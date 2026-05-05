## Progress so far:
- A 700GiB  catalog called `desi-dr1-main-dark` at `/global/cfs/cdirs/cosmo/users/olynn/`
  - covers DESI's **main** survey, **dark** program
- A call to `is_valid_catalog` returns True, 
  - with `5769 partitions` found 
  - and `Approximate coverage is 33.39 % of the sky.`
- Notably we are missing coverage of the galactic plane, 
  - but since our decision (co-working meeting 4/29) to skip the main/bright program and only use main/dark, this is unsurprising

<img width="805" height="440" alt="Image" src="https://github.com/user-attachments/assets/6de43034-c34c-49fa-b308-377538f50d3c" />

- First 5 rows as follows:

<table id="T_ebded">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_ebded_level0_col0" class="col_heading level0 col0" >TARGETID</th>
      <th id="T_ebded_level0_col1" class="col_heading level0 col1" >TARGET_RA</th>
      <th id="T_ebded_level0_col2" class="col_heading level0 col2" >TARGET_DEC</th>
      <th id="T_ebded_level0_col3" class="col_heading level0 col3" >Z</th>
      <th id="T_ebded_level0_col4" class="col_heading level0 col4" >ZERR</th>
      <th id="T_ebded_level0_col5" class="col_heading level0 col5" >spectra_b</th>
      <th id="T_ebded_level0_col6" class="col_heading level0 col6" >spectra_r</th>
      <th id="T_ebded_level0_col7" class="col_heading level0 col7" >spectra_z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ebded_level0_row0" class="row_heading level0 row0" >24531778214</th>
      <td id="T_ebded_row0_col0" class="data row0 col0" >39627785483846048</td>
      <td id="T_ebded_row0_col1" class="data row0 col1" >45.014136</td>
      <td id="T_ebded_row0_col2" class="data row0 col2" >0.019739</td>
      <td id="T_ebded_row0_col3" class="data row0 col3" >1.308415</td>
      <td id="T_ebded_row0_col4" class="data row0 col4" >0.000399</td>
      <td id="T_ebded_row0_col5" class="data row0 col5" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3600.0</td>
      <td>2.924896</td>
      <td>0.327872</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2750 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row0_col6" class="data row0 col6" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5760.0</td>
      <td>1.965631</td>
      <td>7.795724</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2325 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row0_col7" class="data row0 col7" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7520.0</td>
      <td>0.379682</td>
      <td>23.513329</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2880 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
    </tr>
    <tr>
      <th id="T_ebded_level0_row1" class="row_heading level0 row1" >76347715933</th>
      <td id="T_ebded_row1_col0" class="data row1 col0" >39627785483846390</td>
      <td id="T_ebded_row1_col1" class="data row1 col1" >45.027565</td>
      <td id="T_ebded_row1_col2" class="data row1 col2" >0.029181</td>
      <td id="T_ebded_row1_col3" class="data row1 col3" >0.884491</td>
      <td id="T_ebded_row1_col4" class="data row1 col4" >0.000116</td>
      <td id="T_ebded_row1_col5" class="data row1 col5" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3600.0</td>
      <td>-3.560856</td>
      <td>0.253497</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2750 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row1_col6" class="data row1 col6" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5760.0</td>
      <td>0.741585</td>
      <td>0.270924</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2325 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row1_col7" class="data row1 col7" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7520.0</td>
      <td>-0.305626</td>
      <td>5.653226</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2880 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
    </tr>
    <tr>
      <th id="T_ebded_level0_row2" class="row_heading level0 row2" >79430617729</th>
      <td id="T_ebded_row2_col0" class="data row2 col0" >2714981116149760</td>
      <td id="T_ebded_row2_col1" class="data row2 col1" >45.018964</td>
      <td id="T_ebded_row2_col2" class="data row2 col2" >0.029766</td>
      <td id="T_ebded_row2_col3" class="data row2 col3" >0.129609</td>
      <td id="T_ebded_row2_col4" class="data row2 col4" >0.000009</td>
      <td id="T_ebded_row2_col5" class="data row2 col5" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3600.0</td>
      <td>-5.12881</td>
      <td>0.024819</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2750 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row2_col6" class="data row2 col6" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5760.0</td>
      <td>0.757192</td>
      <td>0.056087</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2325 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row2_col7" class="data row2 col7" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7520.0</td>
      <td>0.227893</td>
      <td>10.47636</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2880 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
    </tr>
    <tr>
      <th id="T_ebded_level0_row3" class="row_heading level0 row3" >88592216842</th>
      <td id="T_ebded_row3_col0" class="data row3 col0" >-110547443</td>
      <td id="T_ebded_row3_col1" class="data row3 col1" >45.028689</td>
      <td id="T_ebded_row3_col2" class="data row3 col2" >0.031667</td>
      <td id="T_ebded_row3_col3" class="data row3 col3" >1.499465</td>
      <td id="T_ebded_row3_col4" class="data row3 col4" >0.000098</td>
      <td id="T_ebded_row3_col5" class="data row3 col5" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3600.0</td>
      <td>1.824267</td>
      <td>0.085791</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2750 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row3_col6" class="data row3 col6" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5760.0</td>
      <td>-0.888818</td>
      <td>1.860335</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2325 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row3_col7" class="data row3 col7" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7520.0</td>
      <td>-0.377297</td>
      <td>4.615465</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2880 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
    </tr>
    <tr>
      <th id="T_ebded_level0_row4" class="row_heading level0 row4" >101138674798</th>
      <td id="T_ebded_row4_col0" class="data row4 col0" >39627785483846478</td>
      <td id="T_ebded_row4_col1" class="data row4 col1" >45.030526</td>
      <td id="T_ebded_row4_col2" class="data row4 col2" >0.041094</td>
      <td id="T_ebded_row4_col3" class="data row4 col3" >1.263249</td>
      <td id="T_ebded_row4_col4" class="data row4 col4" >0.000090</td>
      <td id="T_ebded_row4_col5" class="data row4 col5" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3600.0</td>
      <td>0.314766</td>
      <td>0.135213</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2750 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row4_col6" class="data row4 col6" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5760.0</td>
      <td>0.615158</td>
      <td>3.966969</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2325 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row4_col7" class="data row4 col7" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7520.0</td>
      <td>1.088948</td>
      <td>11.775853</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2880 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table>
5 rows x 8 columns
