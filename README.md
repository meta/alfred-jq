alfred-jq
==============
[![Alfred Workflow](https://img.shields.io/badge/Alfred-Workflow-5b2585)](https://alfredapp.com)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/meta/alfred-jq?label=latest%20release)](https://github.com/meta/alfred-meta/releases) 
[![GitHub](https://img.shields.io/github/license/meta/alfred-jq)](https://github.com/meta/alfred-jq/blob/primary/LICENSE) 
[![GitHub stars](https://img.shields.io/github/stars/meta/alfred-jq)](https://github.com/meta/alfred-jq/stargazers)
[![GitHub all releases](https://img.shields.io/github/downloads/meta/alfred-jq/total)](https://github.com/meta/alfred-jq/releases)

Alfred workflow to conveniently process JQ on clipboard based on a jq query
Also available at: [packal/jq]()

# Use case: quick JSON processing/restructuring with jq without terminal
![jq](https://user-images.githubusercontent.com/5732757/139618920-1df38ed6-3b59-4b4c-a89b-ba80897d2a07.gif)


# Install
Use the packaged workflow [jq.alfredworkflow](https://github.com/meta/repository/raw/master/com.meta/jq.alfredworkflow) from packal.

# Requirement
- jq
- alfredworkflow python module (already included) -- Thanks to Dean Jackson: https://github.com/deanishe/alfred-workflow

# How to

## Get the time

- jq (Enter)
- type '.' (available next keys will pops up)
- press TAB to autocomplete (or click option with mouse)
- Enter: preview the resulting jq process on the clipboard json
- Shift-Enter: paste the result back to clipboard


