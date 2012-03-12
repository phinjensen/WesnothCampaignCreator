scenarioRoot = """
[scenario]
    name=
    id=
    turns=
    next_scenario=
    map_data=

    {DEFAULT_SCHEDULE}

"""

side = """
    [side]
        type=
        name=
        id=
        canrecruit=
        unrenamable=
        controller=
        side=
        {GOLD 
        income=
        fog=
        shroud=
        team_name=
        user_team_name=_ "
        recruit=
    [/side]"""

story = """
    [story]

    [/story]"""

storyPart = """
    [part]
        story=_ " "
    [/part]"""

objectivesEvent = """
    [event]
        name=prestart
        [objectives]

        [/objectives]
    [/event]"""

singleObjective = """
            [objective]
                description=_ " "
                condition=
            [/objective]"""

startEvent = """
    [event]
        name=start

    [/event]"""

message = """
        [message]
            speaker=
            message=_ " "
        [/message]"""

lastBreathEvent = """
    [event]
        name=last breath
        [filter]
            id=
        [/filter]

    [/event]"""

endLevel = """
    [endlevel]
        result=

    [/endlevel]"""
