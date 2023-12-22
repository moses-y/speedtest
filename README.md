 # Internet Speed Test Script

This script performs an internet speed test using the `speedtest-cli` command-line tool, parses the results, saves them to a file, and plots the results over time.

## How to Use

## Requirements

1. Before running the script, ensure you have the necessary packages installed. Run the following command:

```
pip install -r requirements.txt

```

2. Clone this repository to your local machine.

3. Open the `speed_test.py` file in your preferred code editor.

4. Run the script by running the following command in your terminal:

```
python speed_test.py
```

The script will perform a speed test and display the results in the terminal. It will also save the results to a file named `speed_test_results.txt` in the same directory as the script.

## Code Explanation

The script consists of the following functions:

* `perform_speed_test()`: This function uses the `subprocess` module to run the `speedtest-cli` command and capture the output as a JSON string. It then parses the JSON string and returns a dictionary containing the download speed, upload speed, and latency.
* `parse_speed_test_result()`: This function takes the dictionary returned by `perform_speed_test()` and extracts the download speed, upload speed, and latency. It returns these values as separate variables.
* `save_speed_test_result()`: This function takes the download speed, upload speed, and latency and saves them to a file named `speed_test_results.txt`. The file is opened in append mode, so each time the function is called, the results are appended to the file.
* `load_speed_test_results()`: This function loads the speed test results from the `speed_test_results.txt` file and returns them as a list of lists. Each list contains the date, download speed, upload speed, and latency for a single speed test.
* `plot_speed_test_results()`: This function takes the list of speed test results and plots them over time. The plot shows the download speed, upload speed, and latency for each speed test.

## Conclusion

This script provides a simple way to perform internet speed tests and track the results over time. It can be used by anyone who wants to monitor their internet connection performance or diagnose issues with their network speed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


