Set-Location -Path e:\IDE\pythonProject\ -PassThru
$comm = '.\venv\Scripts\activate'

& $comm

streamlit run E:\IDE\pythonProject\task_2_web_service.py


Write-Host "Press any key to continue … or Ctrl+C to abort"
$x = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")


