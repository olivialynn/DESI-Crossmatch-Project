from bs4 import BeautifulSoup
import json
import re


def _parse_report(filepath):
    """Parse the Dask performance report HTML and return the summary text."""
    with open(filepath, "r") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    for s in soup.find_all("script", type="application/json"):
        try:
            data = json.loads(s.string)
            uuid = list(data.keys())[0]
            tabs = data[uuid]['roots'][0]['attributes']['tabs']
            for tab in tabs:
                if tab['attributes'].get('title') == 'Summary':
                    return tab['attributes']['child']['attributes']['text']
        except (json.JSONDecodeError, KeyError):
            continue

    raise ValueError("Could not find Summary tab in report.")


def _parse_duration(s):
    """Convert a duration string like '10m 40s' or '4hr 50m' to total seconds."""
    s = s.strip()
    total = 0
    for value, unit in re.findall(r'([\d.]+)\s*(hr|m|s)', s):
        value = float(value)
        if unit == 'hr':
            total += value * 3600
        elif unit == 'm':
            total += value * 60
        elif unit == 's':
            total += value
    return total


def _format_duration(seconds):
    """Format a duration in seconds to a human-readable string."""
    if seconds < 1:
        return f"{seconds*1000:.0f}ms"
    elif seconds < 60:
        return f"{seconds:.2f}s"
    elif seconds < 3600:
        mins = int(seconds // 60)
        secs = seconds % 60
        return f"{mins}m {secs:.0f}s" if secs else f"{mins}m"
    else:
        hrs = int(seconds // 3600)
        mins = int((seconds % 3600) // 60)
        return f"{hrs}hr {mins}m" if mins else f"{hrs}hr"


def _parse_summary_metrics(summary_html):
    """Extract metrics from the summary HTML string."""
    soup = BeautifulSoup(summary_html, "html.parser")
    text = soup.get_text(separator='\n')

    metrics = {}

    # duration
    duration_match = re.search(r'Duration:\s*([\dhrms ]+)', text)
    if duration_match:
        metrics['wall_time'] = duration_match.group(1).strip()

    # tasks
    tasks_match = re.search(r'number of tasks:\s*([\d,]+)', text)
    if tasks_match:
        metrics['total_tasks'] = tasks_match.group(1).strip()

    # compute time
    compute_match = re.search(r'compute time:\s*([\dhrms ]+)', text)
    if compute_match:
        metrics['compute_time'] = compute_match.group(1).strip()

    # transfer time
    transfer_match = re.search(r'transfer time:\s*([\dhrms .]+)', text)
    if transfer_match:
        metrics['transfer_time'] = transfer_match.group(1).strip()

    # disk read
    disk_read_match = re.search(r'disk-read time:\s*([\d. msh]+)', text)
    if disk_read_match:
        metrics['disk_read_time'] = disk_read_match.group(1).strip()

    # disk write
    disk_write_match = re.search(r'disk-write time:\s*([\d. msh]+)', text)
    if disk_write_match:
        metrics['disk_write_time'] = disk_write_match.group(1).strip()

    # workers
    workers_match = re.search(r'Workers:\s*(\d+)', text)
    if workers_match:
        metrics['workers'] = int(workers_match.group(1))

    # threads
    threads_match = re.search(r'Threads:\s*(\d+)', text)
    if threads_match:
        metrics['total_threads'] = int(threads_match.group(1))

    # memory
    memory_match = re.search(r'Memory:\s*([\d.]+ \w+)', text)
    if memory_match:
        metrics['total_memory'] = memory_match.group(1).strip()

    # bandwidth
    bandwidth_match = re.search(r'Bandwidth:\s*([\d.]+ \w+)', text)
    if bandwidth_match:
        metrics['bandwidth'] = bandwidth_match.group(1).strip()

    return metrics


def client_table(filepath, threads_per_worker, memory_limit_per_worker):
    """
    Generate a markdown table of Dask client parameters.

    Parameters
    ----------
    filepath : str
        Path to the Dask performance report HTML file.
    threads_per_worker : int
        Number of threads per worker (from your Client() call).
    memory_limit_per_worker : str
        Memory limit per worker (from your Client() call), e.g. '14 GB'.
    """
    summary_html = _parse_report(filepath)
    metrics = _parse_summary_metrics(summary_html)

    workers = metrics.get('workers', 'N/A')
    total_threads = metrics.get('total_threads', 'N/A')
    total_memory = metrics.get('total_memory', 'N/A')

    lines = [
        "| Parameter | Value |",
        "|---|---|",
        f"| Workers | {workers:,} |",
        f"| Threads per worker | {threads_per_worker} |",
        f"| Total threads | {total_threads:,} |",
        f"| Memory per worker | {memory_limit_per_worker} |",
        f"| Total memory | {total_memory} |",
    ]
    return '\n'.join(lines)


def metrics_table(filepath):
    """
    Generate a markdown table of crossmatch performance metrics.

    Parameters
    ----------
    filepath : str
        Path to the Dask performance report HTML file.
    """
    summary_html = _parse_report(filepath)
    metrics = _parse_summary_metrics(summary_html)

    lines = [
        "| Metric | Value |",
        "|---|---|",
        f"| Total tasks | {metrics.get('total_tasks', 'N/A')} |",
        f"| Wall time | {metrics.get('wall_time', 'N/A')} |",
        f"| Compute time (all workers) | {metrics.get('compute_time', 'N/A')} |",
        f"| Transfer time | {metrics.get('transfer_time', 'N/A')} |",
        f"| Disk read time | {metrics.get('disk_read_time', 'N/A')} |",
        f"| Disk write time | {metrics.get('disk_write_time', 'N/A')} |",
        f"| Total bandwidth | {metrics.get('bandwidth', 'N/A')} |",
    ]
    return '\n'.join(lines)