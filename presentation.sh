#!/bin/bash

# Start a new tmux session
tmux new-session -d -s mypresentation

# Split the window vertically
#tmux split-window -v
# Split the window horizontally 
tmux split-window -h

# Select the first split
tmux select-pane -t 0

# Run the first script in the first split
tmux send-keys "/usr/bin/asciinema play -s 5 1_report_lost_id.rec" C-m

# Select the second split
tmux select-pane -t 1

# Run the second script in the second split
tmux send-keys "/usr/bin/asciinema play -s 5 2_Remitt_Lost_id_to_Huduma_Station.rec" C-m

# Attach to the tmux session to see the presentation
tmux attach-session -t mypresentation

