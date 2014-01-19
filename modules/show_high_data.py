
#!/usr/bin/env python
#
#            --------------------------------------------------
#                            Wireless Forensics Framework
#            --------------------------------------------------
#        Copyright (C) <2014>  <Ap3x Pr3Dat0r (Nipun Jaswal)>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License
#
#    WFF is Wireless Forensics Framework Developed For Penetration Testing and Forensics of Wireless Networks
#
#
#    About Author :
#
#    Founder :Ap3x Pr3Dat0r (Nipun Jaswal)
#    Location : India
#    Email : mail@nipunjaswal.info
#    Blog : www.nipunjaswal.com, www.nipunjaswal.info
################################################################################################################
from core.forensiclib import datalib
def menu_show_high_data():
	option=raw_input('Wff:Forensic:Data>')
        if option=="help" or option=="h":
                print("MAC SPOOF CHECK    Short Hand      Fake MAC Check Options Menu                     ")
                print("================   ==========      =============================                   ")
                print("show data              sdt         Show All Destinations With Fake MAC Detect      ")
		print("go back                 gb         Previous Menu                                   ")
                menu_show_high_data()
	elif option=="show data" or option=="sdt":
                datalib.show_high_data()
                menu_show_high_data()
        elif option=="go back" or option=="gb":
                return
        else:
                menu_show_high_data()
	
