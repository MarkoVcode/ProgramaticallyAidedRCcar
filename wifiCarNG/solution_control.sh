#!/usr/bin/env bash

### BEGIN CONFIGURATION ###
MEDIAMTX_CMD="~/mediamtx ./mediamtx/mediamtx.yml"
SCRIPT1_CMD="python websocketControllerReceiver.py"
SCRIPT2_CMD="python websocketTelemetryTransmitter.py"
### END CONFIGURATION ###

# Where to store PID files
PID_DIR="/tmp"

# PID file names
MEDIAMTX_PID_FILE="$PID_DIR/mediamtx.pid"
SCRIPT1_PID_FILE="$PID_DIR/script1.pid"
SCRIPT2_PID_FILE="$PID_DIR/script2.pid"

start_program() {
  local cmd="$1"
  local pid_file="$2"
  local name="$3"

  # Check if already running
  if [ -f "$pid_file" ] && kill -0 "$(cat "$pid_file")" 2>/dev/null; then
    echo "$name is already running (PID: $(cat "$pid_file"))."
  else
    echo "Starting $name..."
    # Start the process in the background, redirect output if desired
    # (e.g., append to some log file)
    $cmd > /dev/null 2>&1 &
    echo $! > "$pid_file"
    echo "$name started with PID: $(cat "$pid_file")."
  fi
}

stop_program() {
  local pid_file="$1"
  local name="$2"

  if [ -f "$pid_file" ] && kill -0 "$(cat "$pid_file")" 2>/dev/null; then
    echo "Stopping $name (PID: $(cat "$pid_file"))..."
    kill "$(cat "$pid_file")" && rm -f "$pid_file"
    echo "$name stopped."
  else
    echo "$name is not running or PID file not found."
  fi
}

status_program() {
  local pid_file="$1"
  local name="$2"

  if [ -f "$pid_file" ] && kill -0 "$(cat "$pid_file")" 2>/dev/null; then
    echo "$name is running with PID: $(cat "$pid_file")."
  else
    echo "$name is not running."
  fi
}

case "$1" in
  start)
    start_program "$MEDIAMTX_CMD" "$MEDIAMTX_PID_FILE" "mediamtx"
    start_program "$SCRIPT1_CMD"  "$SCRIPT1_PID_FILE"  "script1"
    start_program "$SCRIPT2_CMD"  "$SCRIPT2_PID_FILE"  "script2"
    ;;
  stop)
    stop_program "$SCRIPT2_PID_FILE" "script2"
    stop_program "$SCRIPT1_PID_FILE" "script1"
    stop_program "$MEDIAMTX_PID_FILE" "mediamtx"
    ;;
  status)
    status_program "$MEDIAMTX_PID_FILE" "mediamtx"
    status_program "$SCRIPT1_PID_FILE"  "script1"
    status_program "$SCRIPT2_PID_FILE"  "script2"
    ;;
  *)
    echo "Usage: $0 {start|stop|status}"
    exit 1
    ;;
esac

exit 0

