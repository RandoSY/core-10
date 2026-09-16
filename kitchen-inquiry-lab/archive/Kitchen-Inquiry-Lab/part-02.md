|                        |                                                                                                                                                                                           |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **📊 Data & Analysis** | Calculate: mean, std dev, CV% for M_water series. Plot: reading vs trial number (should be flat). Accept if CV \< 0.5%. Compare M_known to published value — this is your accuracy check. |

|                    |                                                                                                                                                              |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **⚠️ Uncertainty** | Resolution limit (0.1 g) sets floor on uncertainty. Vibration and breath on pan cause noise. Record room conditions. Repeatability ≠ accuracy — both matter. |

|                   |                                                                                                                                                             |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **🚀 Extensions** | Weigh the same object on a second scale and compare. Determine the minimum detectable mass change. Investigate how temperature of the pan affects readings. |

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>TIER 0</strong></p>
<p><strong>0.2</strong></p></td>
<td><strong>Measuring Cup Calibration</strong></td>
</tr>
</tbody>
</table>

|                |                                                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **🎯 Purpose** | Verify printed graduation marks on the eMeasuring Cup using mass-of-water as the ground truth. Treat the printed scale as a hypothesis. |

|                  |                                                                |
|------------------|----------------------------------------------------------------|
| **🔧 Equipment** | eMeasuring Cup · eScale · Water · Eye-level reading discipline |

|              |                                                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| **📐 Model** | For water at ~20°C: 1 mL ≡ 1 g (density ≈ 0.998 g/mL). Therefore mass of water is the reference; cup graduation is the thing being tested. |

|                 |                                                                                                                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **📋 Protocol** | 1\) Tare cup on scale. 2) Add water until meniscus aligns with 100 mL line (read at eye level). 3) Record mass. 4) Repeat for 200, 300, 400, 500, 700, 900 mL. 5) Record actual volume = mass in grams. 6) Calculate error at each graduation. |

|                        |                                                                                                                                                                                   |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **📊 Data & Analysis** | Plot: measured mass vs target volume. Expected slope ≈ 1.00 g/mL. Fit linear regression; slope deviation from 1.00 quantifies systematic bias. Note parallax error at each level. |

|                    |                                                                                                                                                                            |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **⚠️ Uncertainty** | Parallax is the dominant error — must read at eye level. Meniscus bottom is the reading point. Temperature shifts density ~0.1% per °C — negligible here but worth noting. |

|                   |                                                                                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **🚀 Extensions** | Test at different water temperatures. Test a second cup and compare. Calculate what a 5% volumetric error means in a recipe's salt concentration. |

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>TIER 0</strong></p>
<p><strong>0.3</strong></p></td>
<td><strong>Thermometer Validation (Ice Bath + Boiling
Reference)</strong></td>
</tr>
</tbody>
</table>

|                |                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------|
| **🎯 Purpose** | Validate the eThermometer at two fixed points — ice bath (≈0°C) and boiling (≈100°C at sea level, adjusted for altitude). |

|                  |                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------|
| **🔧 Equipment** | eThermometer · eMeasuring Cup or bowl · Ice (crushed or cubed) · Cold water · Kettle or stove · Boiling water |

|              |                                                                                                                                                                                                                            |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **📐 Model** | Phase-change points are thermodynamic constants. Ice-water equilibrium = 0.0°C; boiling water at sea level = 100.0°C (−0.34°C per 100 m altitude). Deviation from these values is instrument error, not measurement error. |

|                 |                                                                                                                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **📋 Protocol** | ICE: 1) Fill cup ~2/3 with crushed ice; add water to cover. 2) Stir 30 s. 3) Insert probe; wait for stable reading (~60 s). 4) Record T_ice every 30 s for 3 min. BOIL: 5) Bring 300 mL water to full rolling boil. 6) Insert probe tip mid-depth. 7) Record T_boil when stable. |

|                        |                                                                                                                                                                                            |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **📊 Data & Analysis** | Calculate offset = T_reading − T_expected at each point. If linear, apply correction: T_true = T_reading − offset. Stabilization time (seconds to within 0.2°C of final) is also key data. |

|                    |                                                                                                                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **⚠️ Uncertainty** | Altitude correction required if \>500 m elevation. Probe placement affects reading — tip must be fully submerged in liquid, not touching container. Allow full stabilization before recording. |

|                   |                                                                                                                                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **🚀 Extensions** | Compare stabilization time for ice vs boiling. Measure room-temperature water and compare to a second thermometer. Deliberately touch the probe to the container wall and observe the artifact. |

|                                 |
|---------------------------------|
| **CORE MEASUREMENT PRINCIPLES** |

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 2%" />
<col style="width: 48%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Controlled Vocabulary</strong></p>
<p>Energy ≠ Power</p>
<p>Repeatability ≠ Accuracy</p>
<p>Calibration ≠ Zeroing</p>
<p>Measurement ≠ Device</p>
<p>Model ≠ Result</p></td>
<td></td>
<td><p><strong>Mass-First Philosophy</strong></p>
<p>Prefer mass over volume for repeatability</p>
<p>1 g ≈ 1 mL ≈ 1 cm³ for water</p>
<p>Volume markings are hypotheses — test them</p>
<p>Log metadata to make results reproducible</p>
<p>Every printed label is a claim to be verified</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>STATE SNAPSHOT TEMPLATE</strong></p>
<p>Lab Version: ___ | Date: ___ | Instruments confirmed: ☐ Scale ☐
Thermometer ☐ Cup ☐ WattMinder ☐ Timer</p>
<p>Calibration Status: ___ | Ambient Temp (°C): ___ | Altitude (m):
___</p>
<p>Current Experiment: ___ | Last Dataset (label): ___</p>
<p>Key Results: ___ | Known Issues / Quirks: ___</p>
<p><em>Next Step: ___ (include setup notes — this snapshot must allow a
full cold restart)</em></p></td>
</tr>
</tbody>
</table>
