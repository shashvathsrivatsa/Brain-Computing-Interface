from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

# Set the board ID for Cyton board
# board_id = BoardIds.CYTON_BOARD
# params = BrainFlowInputParams()
# params.serial_port = '/dev/ttyUSB0'  # Adjust the serial port based on your device
# params.sampling_rate = 256  # Set the desired sampling rate

# Example board
board_id = BoardIds.SYNTHETIC_BOARD

# Initialize BrainFlow board
params = BrainFlowInputParams()
params.sampling_rate = 256  # Set the desired sampling rate

board = BoardShim(board_id, params)

# Set up streaming + start acquisition
board.prepare_session()
board.start_stream()

# Read data
num_samples = 1000  # Adjust the number of samples as needed
data = []

try:
    while len(data) < num_samples:
        # Read the latest data
        current_data = board.get_current_board_data(256)  # You can adjust the number of samples per read
        data.extend(current_data[0])  # Assuming you're using a single channel, adjust if using multiple channels

except KeyboardInterrupt:
    pass  # Stop the loop if the user interrupts (Ctrl+C)

finally:
    # Stop streaming + release resources
    board.stop_stream()
    board.release_session()

# Return the data
def getData():
    return data
