# valorantbp

I used this [video](https://www.youtube.com/watch?v=0RxYsb4Rtbw) as the basis for how much points you can get daily if you played efficiently each day.
It calculates how much exp you can expect to gain, how much exp is left in the battlepass, and how much additional exp is needed to close out the bp.

## usage

```text
usage: valorantbp [-h] [--version] [-e EPILOGUE] [-c CURRENT] [-d DAYS] [-w WEEK] [-m MISSION] [-t TIER]
                  [--edays EDAYS] [--event] [--reset] [--show] [--before]

Track Valorant BattlePass

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --event               Track event progress
  --reset               Reset tracker progress
  --show                Show current tracker config
  --before              Show previous tracker event progress before update

battlepass:
  Directly updates individual settings for tracking the battlepass

  -e EPILOGUE, --epilogue EPILOGUE
                        Current epilogue in progress
  -c CURRENT, --current CURRENT
                        Current exp progress in current tier
  -d DAYS, --days DAYS  How many days are left in the battlepass
  -w WEEK, --week WEEK  Current week of weekly missions in progress
  -m MISSION, --mission MISSION
                        Number of current weekly missions left in current week
  -t TIER, --tier TIER  Current completed tier in battlepass
  --edays EDAYS         How many days left in event battlepass
 ```

## Examples

- Let's track my current progress:

    ```console
    $ valorantbp
    Expected exp to gain: 231240
    Progress exp left: 239440
    Progress to work on: 8200
    ```

    The "Expected exp to gain" shows how much exp I can expect to gain from the remaining daily and weekly missions.
    The "Progress exp left" shows how much exp is left in battlepass until completion.
    The "Progress to work on" shows how much exp is needed to be grinded outside of the missions e.g. a subtraction of the two aforementioned numbers.

- To see a more verbose tracking output of the battlepass, use `--show`

    ```console
    $ valorantbp --show
    {
        "epilogue": 0,
        "current": 18310,
        "days": 15,
        "week": 6,
        "mission": 3,
        "tier": 48
    }
    Expected exp to gain: 231240
    Progress exp left: 239440
    Progress to work on: 8200
    ```

    This output shows the additional variables used to calculate the three numbers at the bottom.
    `epilogue` shows the number of completed epilogue tiers in the battlepass.
    `current` shows the progress in the current tier.
    `days` shows how many days are left in the battlepass.
    `week` shows the current week of the weekly missions.
    `mission` shows the number of weekly missions are left in the current week.
    `tier` shows the number of completed tiers in the battlepass.

## FAQ

1. Can I complete the battlepass if I play efficiently i.e. only playing to the daily and weekly missions?

As of Episode 7, you now can. Valorant has replaced its daily missions with a daily counter: you need to win 16 rounds (from unrated, comp, or swiftplay) and/or play 8 matches (in spike rush or TDM) to complete your dailies now. That results in a daily 12,000 exp in the battlepass which usually helps complete the battlepass if you are diligent from day one.
