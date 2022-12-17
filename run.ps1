$d = Start-Job -ScriptBlock {python .\receive.py}
python .\send.py
Receive-Job $d
Remove-Job $d
