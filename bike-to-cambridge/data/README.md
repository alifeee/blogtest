# GPX data

This file holds a lot of gpx data. For quick viewing of a file, you can import it into [gpx-studio].

[gpx-studio]: https://gpx.studio/

## Short names

Where names are briefened, the following short names are used:

| Short name | Location |
| ---------- | -------- |
| `BHM`      | Birmingham |
| `STR`      | Stratford-upon-Avon |
| `LEA`      | Leamington Spa |
| `BIC`      | Bicester |
| `BED`      | Bedford |
| `SAN`      | Sandy |
| `CAM`      | Cambridge |

## Bike routes (`./bike/`)

These are obtained from OS maps. They were originally recorded as 'activities', but were transitioned to 'routes', so they could be exported as GPX. This meant that they lost the information about time taken.

### `BHM_to_STR`

### `BIC_to_BED`

### `BED_to_SAN`

## Train routes (`./train/`)

These are obtained from BRouter. For example: [Stratford-upon-Avon to Leamington Spa][brouter-str-lea].

### `STR_TO_LEA`

### `LEA_TO_BIC`

### `SAN_TO_CAM`

[brouter-str-lea]: https://brouter.damsy.net/latest/#map=12/52.2496/-1.5661/standard&lonlats=-1.716399,52.194352;-1.535811,52.284636&profile=rail

## Cycle travel route (`./cycle.travel/`)

### `BHM_to_CAM`

The route is created on [cycle.travel] and exported as GPX. Cycle travel only allows sharing the [start- to end-point][ct-route] (the middle points are not sharable via link).

### `BHM_to_CAM_from_google`

This route is created by importing the gpx from the [google maps route](#google-maps-route-google) into [cycle.travel] and tracing the route.

[cycle.travel]: https://cycle.travel/map
[ct-route]: https://cycle.travel/map?from=Birmingham%20New%20Street&to=All%20Seasons%20Guest%20House&fromLL=52.4776459,-1.898694&toLL=52.21544625,0.1298144315358627

## Google maps route (`./google/`)

[Birmingham to Cambridge via stopovers][google-route]

[google-route]: https://www.google.co.uk/maps/dir/Birmingham+New+Street,+Station+Street,+Birmingham/The+Dice+Box,+Regent+Street,+Leamington+Spa/52.3148143,-0.7141751/The+Kent+Arms,+Salisbury+Street,+Bedford/St+Regis,+Cambridge+CB4+1BZ/@52.2941527,-1.0933319,10.17z/data=!4m27!4m26!1m5!1m1!1s0x487096f1df0e0571:0xedfa487a0f2ea32e!2m2!1d-1.898958!2d52.477754!1m5!1m1!1s0x4877352da2a0fce3:0xce78debaf07606df!2m2!1d-1.5329032!2d52.2906199!1m0!1m5!1m1!1s0x4877b6d784178951:0x26fc2ce9fea12cb8!2m2!1d-0.4706178!2d52.145602!1m5!1m1!1s0x47d870eda7b78ed3:0xd72312dabea43338!2m2!1d0.1303911!2d52.2151941!3e1

## Route metadata

For some routes, metadata is provided, which is copied from the [cycle.travel] website. This is provided as a `json` file adjacent to the `gpx` file.

![cycle.travel route metadata](./images/cycle.travel%20metadata.png)

### JSON example

```json
{
  "total_length": 211,
  "total_time": "13:28",
  "road_types": {
    "busy_road": 2.4,
    "paved_road": 155,
    "paved_path": 48.3,
    "unpaved_path": 5.3,
    "pushing": 0.58
  }
}
```
