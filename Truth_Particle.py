#Import package
    import os
    import pandas as pd
    import uproot
    import numpy as np
    
    #Load root file
    root_file = "/root/Delphes-3.4.2/output2.root"
    file = uproot.open(root_file)
    
    #show the branch in Delphes;1
    file["Delphes;1"].show()
    
    event = [file["Delphes;1"]["Particle.Status"].array(),
             file["Delphes;1"]["Particle.M1"].array(),
             file["Delphes;1"]["Particle.M2"].array(),
             file["Delphes;1"]["Particle.D1"].array(),
             file["Delphes;1"]["Particle.D2"].array(),
             file["Delphes;1"]["Particle.PID"].array(),
             file["Delphes;1"]["Particle.PT"].array(),
             file["Delphes;1"]["Particle.Eta"].array(),
             file["Delphes;1"]["Particle.Phi"].array(),
             file["Delphes;1"]["Particle.Mass"].array(),
             ]
             #Reshape the datastructure
             event = np.expand_dims(event, axis=-1)
             event = event.transpose((1,0,2))
             event = np.squeeze(event,axis=(2,))
             _Status, _M1, _M2, _D1, _D2, _PID, _PT, _Eta, _Phi, _Mass = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
             Labels = ["Status", "M1", "M2", "D1", "D2", "PID", "PT", "Eta", "Phi", "Mass"]
             
             #Show truth record
             print("Index", "\t","Status", "\t","M1"
                   "\t","M2" ,"\t","D1", "\t","D2", "\t","PID",
                   "\t\t","PT" "\t","Eta", "\t\t","Phi",
                   "\t\t","Mass")
             
             for j in range(len(event[0][0])):
                 print(j, "\t", event[0][_Status][j],"\t\t",
                       event[0][_M1][j], "\t", event[0][_M2][j],
                       "\t", event[0][_D1][j], "\t", event[0][_D2][j],
                       "\t", str(event[0][_PID][j]).ljust(12, ' '), "\t", round(event[0][_PT][j],0),  "\t",
                       str(round(event[0][_Eta][j],2)).ljust(12, ' ') , "\t",
                       str(round(event[0][_Phi][j],3)).ljust(12, ' '), "\t",
                       round(event[0][_Mass][j],3))
