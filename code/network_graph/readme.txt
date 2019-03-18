To process new data. First arrange the data into a csv adjancy matrix. 

Put the data into adjancencyMatrixToNetGraphJson folder and open the folder and in main.py change the file filename on line 10 from out.csv to the name of your file. 

If you want to add custom data to the nodes, add it to the nodes class in netgraphjson.py. 

Run python main.py using python 3.4 >=

The output will be netgraphjson.json. 

Take the output file and place it in netjsongrpah folder. 

From there you should be able to run "python -m http.server" in a terminal and view the output at localhost:8000. 

To change the color choices go to netjsongraph.js line 456 and you can edit the array of colors. 

For more information or examples on NetJsonGraph visit https://github.com/netjson/netjsongraph.js/blob/master/README.rst


