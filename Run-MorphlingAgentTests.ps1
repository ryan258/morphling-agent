<#
.SYNOPSIS
    Runs the advanced_morphling_agent.py script in a loop for a list of questions, saving logs for each run.

.DESCRIPTION
    This script automates the process of testing the advanced_morphling_agent.py Python script with a series of questions.
    It iterates through a predefined list of questions, executes the Python script for each question,
    and saves the detailed logs for each run to separate files in the 'log' directory.
    This helps in systematically evaluating the agent's performance across different questions.

.NOTES
    Before running this script:
    1. Ensure you have Python and the required Python packages (including 'ollama' and 'openai') installed in your 'someuv' virtual environment.
    2. Activate your 'someuv' virtual environment in the Powershell session where you will run this script.
    3. Modify the '$questions' array in the script to include the questions you want to test.
    4. Verify that the 'advanced_morphling_agent.py' script is in the same directory as this Powershell script, or adjust the '$pythonScriptPath' variable accordingly.

    To activate your 'someuv' virtual environment in Powershell, you typically use:
    `.\someuv\Scripts\Activate.ps1`

    To run this Powershell script, navigate to the script's directory in Powershell and execute:
    `.\Run-MorphlingAgentTests.ps1`

.EXAMPLE
    # Example questions are pre-filled in the script.
    # After activating 'someuv' and running this script, it will:
    # 1. Run advanced_morphling_agent.py for each question in the '$questions' array.
    # 2. Save log files in the 'log' directory, named with the question and timestamp.
    # 3. Display a summary message in the console after each run.
#>

# ----- Configuration -----
$pythonScriptPath = ".\advanced_morphling_agent.py"  # Path to your Python script (adjust if needed)
$questions = @(
    "What is the meaning of life?",
    "What are the best sci-fi movies of the 21st century?",
    "Give me some tips for writing a compelling Piece Of flash fiction",
    "Tell me a funny riddle",
    "Why the cookie with the cookie girl the doctor"
    # Add more questions to test here
)
# ----- End Configuration -----

Write-Host "Starting Morphling Agent Test Runs..." -ForegroundColor Green

foreach ($question in $questions) {
    Write-Host ""  # Add an empty line for better readability in the console
    Write-Host "--- Running test for question: '$question' ---" -ForegroundColor Cyan

    # Sanitize question for filename (remove spaces and special characters)
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $logFileNameSanitized = $question -replace '[^a-zA-Z0-9]', '_' -replace '\s+', '_'
    $logFilePath = Join-Path -Path "log" -ChildPath ("morphling_agent_test_log_{0}_{1}.md" -f $logFileNameSanitized, $timestamp)

    Write-Host "Executing Python script..." -ForegroundColor Gray
    # Execute the Python script, passing the question as input and redirecting output to log file
    try {
        # Use -NoProfile to avoid potential profile loading issues in automated scripts
        # Use -ExecutionPolicy Bypass if needed for script execution permissions
        python -NoProfile -ExecutionPolicy Bypass -File $pythonScriptPath -InputObject $question *>&1 | Tee-Object -FilePath $logFilePath

        Write-Host "Test run for question: '$question' completed successfully. Log saved to: '$logFilePath'" -ForegroundColor Green
    }
    catch {
        Write-Error "Error running script for question: '$question': $($_.Exception.Message)"
        Write-Warning "Check the console output and potential Python script errors."
    }

    Write-Host "--- Test run for question: '$question' finished ---" -ForegroundColor Cyan
}

Write-Host "" # Add an empty line at the end
Write-Host "Morphling Agent Test Runs Completed." -ForegroundColor Green
Write-Host "Please check the 'log' directory for detailed log files." -ForegroundColor Green