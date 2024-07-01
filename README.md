# Cmc_Scrape_Top10_HeatMap_TreeMap
A better visual representation of the CMC top10 gainers in a 24h interval
Uses selenium and there are two types of results you can get:
>A static treemap - uses sqarify and matplotlib to plot
>A dynamic treemap where you have to hover your cusor to display each section details and it reloads in an interval- uses plotly to plot


# Prerequisite
I assume you know how to install and setup webdriver, either firefox or chrome. you first need to download webdriver for your os/browser and then place it in a directory
> see: https://www.selenium.dev/documentation/webdriver/

# Requirements:
webdriver selenium numpy pandas time datetime squarify plotly

Didn't really encounter any issues while trying to plot, I only just realized that what I was trying to do is call a TREEMAP not HEATMAP really lol 😉

For the best view I'd suggest the Jupyter Notebook version

> The Static TreeMap
![HM static](https://github.com/AyFait/Cmc_Scrape_Top10_HeatMap_TreeMap/assets/50885913/848f5ba6-4313-41dc-8098-47065584f559)

> The Dynamic TreeMap
![CmcTrymap Dy Jup](https://github.com/AyFait/Cmc_Scrape_Top10_HeatMap_TreeMap/assets/50885913/bcbdeac0-d2f9-430b-8486-b35e9721c433)
![CMC TM dy vs](https://github.com/AyFait/Cmc_Scrape_Top10_HeatMap_TreeMap/assets/50885913/e7f0be39-8883-45cd-b4a6-8b98b8f1c415)
