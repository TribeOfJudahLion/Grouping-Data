<br/>
<p align="center">
  <a href="https://github.com/TribeOfJudahLion/Grouping-Data">
    <img src="" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Data-Driven Marketing Insights with Python

</h3>

  <p align="center">
    Harness the power of Python to analyze marketing campaign data and unlock actionable insights.
    <br/>
    <br/>
    <a href="https://github.com/TribeOfJudahLion/Grouping-Data"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/TribeOfJudahLion/Grouping-Data">View Demo</a>
    .
    <a href="https://github.com/TribeOfJudahLion/Grouping-Data/issues">Report Bug</a>
    .
    <a href="https://github.com/TribeOfJudahLion/Grouping-Data/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/TribeOfJudahLion/Grouping-Data/total) ![Contributors](https://img.shields.io/github/contributors/TribeOfJudahLion/Grouping-Data?color=dark-green) ![Issues](https://img.shields.io/github/issues/TribeOfJudahLion/Grouping-Data) ![License](https://img.shields.io/github/license/TribeOfJudahLion/Grouping-Data) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Statement

A marketing team at a retail company is seeking to understand customer purchasing patterns to tailor their campaigns more effectively. They have compiled a dataset, `marketing_campaign.csv`, containing various customer attributes and purchasing data. The team needs to load, preprocess, and analyze this data to derive insights. 

However, the team members are not proficient in programming. They require an automated solution that can handle the following tasks:

1. **Loading Data**: Read the dataset from a CSV file safely, ensuring that the file exists and is correctly formatted.

2. **Preprocessing**: Filter out unnecessary data to focus on the following columns:
   - 'ID'
   - 'Year_Birth'
   - 'Education'
   - 'Marital_Status'
   - 'Income'
   - 'Kidhome'
   - 'Teenhome'
   - 'Dt_Customer'
   - 'Recency'
   - 'NumStorePurchases'
   - 'NumWebVisitsMonth'

3. **Analysis**:
   - Display the first 2 rows of the dataset for a quick inspection.
   - Display the data types of each column to verify the data integrity.
   - Display the shape of the dataset for a summary view of data size.
   - Calculate and display the average number of store purchases made by customers grouped by the number of kids in the home.

4. **Logging**: Any errors or significant events should be logged with appropriate messages for troubleshooting and audit trails.

### Solution

To address the needs of the marketing team, a Python script was developed. The script performs the required data loading, preprocessing, and analysis with minimal user intervention. The solution encapsulates functionality into functions, leverages logging for error handling, and uses the Pandas library for data manipulation. The script also checks for file existence before attempting to load data to avoid runtime errors.

#### Implemented Script Breakdown:

- `load_data(file_path)`: This function attempts to load the dataset from the specified CSV file path, logging the status. It catches `FileNotFoundError` to handle cases where the file path is incorrect or the file is missing, and a general `Exception` for any other issues that may arise during loading.

- `preprocess_data(data)`: Given the loaded DataFrame, this function selects only the relevant columns required for analysis. This helps in focusing on the essential data and can improve performance by reducing memory usage.

- `analyze_data(data)`: This function performs several analyses:
   - It prints the transpose of the first 2 rows of the dataset to inspect individual entries clearly.
   - It prints the data types of all the columns to verify if they are loaded in the correct format.
   - It prints the shape of the dataset to give an immediate sense of the dataset's size.
   - It calculates the average number of store purchases by customers, grouped by the number of kids at home, to provide insights into customer behavior.

- `main()`: This orchestrator function defines the path to the CSV file and ensures it exists before proceeding with the loading and analysis functions.

- `if __name__ == "__main__":` Block: This ensures that `main()` is only called when the script is run directly (not when imported as a module).

Upon running the script, the marketing team will receive console output that succinctly displays the key insights they are interested in. Any errors will be logged with an appropriate message, so they can be addressed without needing to dig through the code.

#### Output Expected:

- First 2 rows of the dataset printed in a transposed table for readability.
- Data types for each column to confirm data consistency.
- Shape of the dataset providing the number of rows (entries) and columns (features).
- Average number of store purchases grouped by 'Kidhome', which can guide marketing strategy.

This script would be a foundational tool for the marketing team's data-driven approach, allowing for repeatable, consistent analysis as their dataset grows or changes over time.
### Detailed Solution Based on Output

The Python script designed to load, preprocess, and analyze the `marketing_campaign.csv` dataset has been successfully executed, providing the following detailed solutions to the marketing team:

1. **Data Loading**:
   - The dataset was loaded successfully as indicated by the informational log entry timestamped at `2023-11-07 08:59:20,265`, confirming the file was found and properly read. The shape of the dataset is reported to be `(2240, 30)`, indicating there are 2240 entries across 30 columns.

2. **Preprocessing**:
   - The data was effectively filtered to retain only the columns relevant to the analysis, reducing the dataset to 11 columns. This focus allows the team to direct their attention to crucial variables without the distraction of extraneous information.

3. **Data Analysis Results**:
   - **Initial Data Inspection**:
     - The transposition of the first 2 rows was printed, which allows for a clearer comparison between individual entries across different attributes. This quick inspection could help in spotting any glaring discrepancies or anomalies in the data.

   - **Data Types Verification**:
     - The data types for each column were printed. The output shows a mix of integers (`int64`), floating-point numbers (`float64`), and objects (typically strings, `object`) which is consistent with what one would expect for such a dataset. This step is crucial to ensure that the data is correctly interpreted for any subsequent analysis.

   - **Dataset Size**:
     - The shape of the preprocessed dataset is `(2240, 11)`, reiterating that there are 2240 entries, but now only across 11 columns after preprocessing.

   - **Behavioral Insight**:
     - The average number of store purchases based on the number of kids in the home was calculated. The results suggest that customers with:
       - **No kids (`0`)** have an average of **7.22 store purchases**.
       - **One kid (`1`)** average **3.86 store purchases**.
       - **Two kids (`2`)** average **3.44 store purchases**.
     - This finding is particularly insightful for the marketing team, as it highlights a potential inverse relationship between the number of children in the home and the frequency of store purchases. Such information could be instrumental in crafting targeted marketing campaigns or promotions.

4. **Logging**:
   - The program concluded without any errors as there's no error log present in the output, and the process finished with exit code 0, denoting a successful execution.

#### Conclusion:
The execution of the Python script has provided the marketing team with concrete insights. The team now knows that customers without kids tend to make more purchases in-store, and as the number of kids increases, the number of store purchases tends to decrease. This kind of data-driven analysis can inform the team's strategy, potentially leading to more effective marketing efforts aimed at different segments of their customer base. The smooth execution of the script also demonstrates the robustness of the code in terms of error handling and logging, ensuring that any issues can be quickly identified and resolved.
















## Built With

This section lists the major frameworks and libraries that were utilized in the creation of the project. Here are the key components:

- **[Python](https://www.python.org/)** - A high-level, interpreted, and dynamic programming language that emphasizes readability.
  
- **[Pandas](https://pandas.pydata.org/)** - An open-source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
  
- **[NumPy](https://numpy.org/)** - A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

- **[Logging](https://docs.python.org/3/library/logging.html)** - A module included in Python's standard library, which provides a flexible framework for emitting log messages from Python programs.

- **[sys](https://docs.python.org/3/library/sys.html)** - This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

- **[Pathlib](https://docs.python.org/3/library/pathlib.html)** - An object-oriented filesystem path library that enables you to work with file paths effectively.

For each of these, you can find more information, including how to install and utilize them in your projects, through their respective links. These libraries and tools form the backbone of the project, ensuring that data analysis tasks are performed efficiently and effectively.Here are a few examples.

## Getting Started

This section will guide you through the initial setup and execution of the Python script for analyzing marketing campaign data. Please follow the steps below to ensure that you can run the script on your local machine without any issues.

#### Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

1. **Python**: The script is written in Python, so you will need Python 3.6 or higher. You can download it from the [official Python website](https://www.python.org/downloads/).
   
2. **Pandas Library**: This script utilizes the Pandas library for data manipulation and analysis. You can install it using pip (Python's package installer). Run the following command in your terminal:
   
   ```
   pip install pandas
   ```

3. **NumPy Library**: Although not directly used in the script, Pandas depends on NumPy, so it must also be installed. Typically, installing Pandas via pip should automatically install NumPy. If not, run the following command:
   
   ```
   pip install numpy
   ```

4. **Git**: To clone the repository, you need Git installed on your computer. Download and install it from [Git's website](https://git-scm.com/downloads).

#### Installation

1. **Clone the GitHub Repository**:
   
   Use Git to clone the repository's code to your local machine. Open your terminal, navigate to the directory where you want the project files to be copied, and run:

   ```
   git clone https://github.com/your-username/your-repository.git
   ```

   Replace `your-username` and `your-repository` with the actual username and repository name where the script is hosted.

2. **Navigate to the Project Directory**:

   Once the repository is cloned, navigate to the project directory:

   ```
   cd your-repository
   ```

3. **Dataset**:

   The script requires a dataset named `marketing_campaign.csv` to be present in the project directory. Ensure that this file is available. If the dataset needs to be downloaded or moved to the project directory, complete this step before running the script.

#### Running the Script

1. **Activate a Virtual Environment** (Optional):

   If you are using a virtual environment, activate it with:

   ```
   source venv/bin/activate  # On Unix or MacOS
   venv\Scripts\activate     # On Windows
   ```

   If you haven't created a virtual environment, you can skip this step or create one with:

   ```
   python -m venv venv
   ```

2. **Execute the Script**:

   To run the script, use the following command in the terminal:

   ```
   python advanced_analysis.py
   ```

   Ensure you are in the same directory as the `advanced_analysis.py` script when you run this command.

#### Verifying the Output

After running the script, verify the output in the terminal. It should display:

- The first two rows of the dataset in a transposed view.
- The data types of the dataset's columns.
- The shape of the dataset after preprocessing.
- The average number of store purchases based on the number of kids in the home.

#### Troubleshooting

- If you encounter any `ModuleNotFound` errors, ensure that you have installed all required libraries and that you are running the script using the correct version of Python.
- If the script can't find the dataset file, check the file's path and name in the script. It should be located in the same directory as the script, unless specified otherwise.

By following these instructions, you should be able to set up and run the Python script successfully for marketing campaign data analysis. For further assistance or to report an issue, please use the 'Issues' section of the GitHub repository where the code is hosted.

## Usage

This section guides you through the steps to utilize this Python script to load, preprocess, and analyze marketing campaign data, extract meaningful insights, and understand consumer behavior patterns.

#### Prerequisites
Before you begin, ensure you have the following prerequisites installed:
- Python 3.x
- Pandas library
- NumPy library

If not already installed, you can install them using pip:

```bash
pip install numpy pandas
```

#### Installation
1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repository.git
```

2. Navigate to the cloned repository:

```bash
cd your-repository
```

#### Setting up the Dataset
Place your `marketing_campaign.csv` file in the root directory of the project or specify the path when calling the script.

#### Running the Script
To execute the script, run the following command in your terminal:

```bash
python marketing_analysis.py
```

#### Understanding the Output
The script performs several functions, with the output for each provided sequentially:

1. **Data Loading**: The script will attempt to load the dataset. If successful, a log entry is created indicating successful loading along with the shape of the dataset. In case of a failure, an appropriate error message will be logged.

2. **Data Preprocessing**: Selects relevant columns from the dataset, preparing it for analysis. This operation is silent, but the effects are seen in subsequent outputs.

3. **Data Inspection**:
    - The first two rows of the preprocessed dataset are printed transposed for better readability.
    - The data types of each column in the dataset are displayed.

4. **Dataset Shape**: The script prints the shape of the preprocessed dataset, giving you an idea of its dimensions.

5. **Data Analysis**:
    - Computes and prints the average number of store purchases made by customers, grouped by the number of kids at home.

#### Example Output
Here's an example of what the output might look like:

```plaintext
First 2 rows of the dataset:
                            0           1
ID                       5524        2174
...

Data types of the dataset:
ID                     int64
...

Shape of the dataset:
(2240, 11)

Average number of store purchases based on number of kids in the home:
Kidhome
0    7.217324
1    3.863181
...
```

This output can now be used to make informed decisions about marketing strategies, tailor specific campaigns towards segments of the consumer base, and improve overall customer engagement.

#### Extending the Script
Feel free to modify the script to include additional analyses or to handle different datasets. You can customize the preprocessing steps, add new data columns for analysis, or extract other statistical measures. The modular design makes it easy to extend functionality without disrupting the existing workflow.

---

For any queries or issues regarding the usage of the script, please open an issue on the GitHub repository, and we will address it promptly. Happy analyzing!

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/TribeOfJudahLion/Grouping-Data/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/TribeOfJudahLion/Grouping-Data/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/TribeOfJudahLion/Grouping-Data/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion/) - **

## Acknowledgements

* []()
* []()
* []()
