# FOSS Post Collapse Monitor

![https://i.imgur.com/LSyMWEe.png](https://i.imgur.com/LSyMWEe.png)

Simple out-of-the-box browser for collapse maps worldwide.

There are many indicators for a possible collapse in human civilization, motivated by climate change and other elements. Many people started carefully monitoring these elements in order remain alerted as much as possible, and make sure they are prepared for what is to come.

One can find many useful interactive maps online for this, but you don't always want to open them manually each time you want to check them. Additionally, you may want to keep your markings/edits on some of them (Which may support that unlike the others), and hence, putting all these maps in a different standalone window would give the best experience.

This is the idea of this small app; it is a web browser with 7 maps (Currently) which show different hazards alerts, disaster alerts, future projections for areas with high probability of floodings, earthquakes, natural disasters and many other interesting data.

The following maps are included:
* Emergency and Disaster Information Service (RSOE): https://rsoe-edis.org/eventMap
* Natural Hazards Map (FML Global): https://www.fmglobal.com/research-and-resources/nathaz-toolkit/flood-map
* Disaster Alert (Pdc.org): https://disasteralert.pdc.org/disasteralert
* USA Disaster and Risk Mapping (NCEI): https://www.ncei.noaa.gov/access/billions/mapping
* Aqueduct Maps (Wri.org) (Note: We included the URL to the tools page so that you choose the map you want from the 4 maps they offer): https://www.wri.org/aqueduct/tools
* IPCC WGI Interactive Atlas (IPCC.ch): https://interactive-atlas.ipcc.ch/regional-information
* Earth 2050 (Kaspersky): https://2050.earth

If you restart the app, then you will lose your progress (Which is why we have removed the close button, to make it more difficult to close the app), but if you don't, then you can track the variables/elements that you specify from any of these interactive maps without having to open their websites every time you want to check them.

The software is licensed under the GPLv3 license. Written in Python and WebKitGtk2. Currently the code is not in best shape (So many duplication and lazy coding), but it does the job for a small app like this.
