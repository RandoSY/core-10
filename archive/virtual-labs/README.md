# Recovered Virtual Laboratories

This directory preserves runnable browser laboratories recovered from earlier CORE / UMA work.

## Naming rule

Some artifacts retain `CORE12` in their filename or interface because that was their historical name when created. The current canonical curriculum root is **CORE 10**. Historical names are preserved for provenance; they are not evidence of a competing current architecture.

## Recovered artifacts

### `core12_heater_dashboard.html`

Self-contained browser thermal-plant and heater-control laboratory recovered from the owner’s Library. It includes:

- lumped thermal plant `Cth*dT/dt = Qin - (T-Tamb)/Rth`;
- thermostat, PID, and open-loop controller modes;
- adjustable power, efficiency, ambient temperature, thermal resistance/capacitance, sensor lag, setpoint, hysteresis, duration, and time step;
- optional ambient disturbance;
- temperature, heat-flux, controller, and residual plots;
- measured CSV import and model-vs-data residual/RMSE analysis;
- CSV, JSON, configuration, and chart export;
- no external JavaScript dependencies.

**Recovery status:** runnable source recovered. Hardware-independent browser model; it should not be confused with proof of a particular physical heater implementation.
