
<p align="center">
  <a href="https://fosspost.org">
    <img src="https://i.imgur.com/arbwjkS.png" width="256"/>
  </a>
</p>

# FOSS Post Collapse Monitor

> The world has changed. I see it in the water. I feel it in the Earth. I smell it in the air. Much that once was, is lost. For none now live, who remember it. - J. R. R. Tolkien.

Simple out-of-the-box browser for collapse maps worldwide.

![https://i.imgur.com/LSyMWEe.png](https://i.imgur.com/LSyMWEe.png)



There are many indicators for a [possible collapse in human civilization](https://www.reddit.com/r/collapse), motivated by climate change and other elements. Many people started carefully monitoring these elements in order remain alerted as much as possible, and make sure they are prepared for what is to come.

One can find many useful interactive maps online which provide alerts about possible hazards, accidents and natural disasters, but you don't always want to open them manually each time you want to check them. Additionally, you may want to keep your markings/edits on some of them (Which may support that unlike the others), and hence, putting all these maps in a different standalone window would give the best experience.

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

![https://i.imgur.com/BkJTeOq.jpeg](https://i.imgur.com/BkJTeOq.jpeg)

### Installation

The application is quite simple.

For Debian-based and Ubuntu-based distributions, you can download it as a [DEB package from the releases page](https://github.com/fosspost/fp-collapse-monitor/releases). Then, to install it just run:

```bash
sudo dpkg -i <replace_with_path_to_deb_file>
```

And you'll see it in the applications menu so that you can launch it.

For other distributions, make sure that you have the `python3, python3-gi, gir1.2-webkit2-4.0` packages installed (Or what corresponds to them on your distribution), and then you can simply run the application with:

```python
python fp-collapse-monitor
```

### License & Contribution

The software is licensed under the GPLv3 license. Written in Python and WebKitGtk2. Currently the code is not in best shape (So many duplication and lazy coding), but it does the job for a small app like this.

Please do not try to submit a pull request. If you have anything to comment on then open an issue.

Developed mainly for the audience of FOSS Post: https://fosspost.org
