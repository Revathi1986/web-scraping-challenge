{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import time\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "#i am saving the output of the file.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 91.0.4472\n",
      "Get LATEST driver version for 91.0.4472\n",
      "Driver [C:\\Users\\sunda\\.wdm\\drivers\\chromedriver\\win32\\91.0.4472.101\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url='https://redplanetscience.com'\n",
    "browser.visit(url)\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "html= browser.html\n",
    "soup = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"NASA's MAVEN Observes Martian Night Sky Pulsing in Ultraviolet Light\""
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#got title of the page\n",
    "titles =soup.find('div',class_='content_title').get_text()\n",
    "titles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Vast areas of the Martian night sky pulse in ultraviolet light, according to images from NASA’s MAVEN spacecraft. The results are being used to illuminate complex circulation patterns in the Martian atmosphere.'"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#got paragraph \n",
    "article_teaser_body = soup.find('div', class_ = 'article_teaser_body').get_text()\n",
    "article_teaser_body"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 91.0.4472\n",
      "Get LATEST driver version for 91.0.4472\n",
      "Driver [C:\\Users\\sunda\\.wdm\\drivers\\chromedriver\\win32\\91.0.4472.101\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import time\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "url='https://spaceimages-mars.com'\n",
    "browser.visit(url)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "full_image_elem = browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "img_soup = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://spaceimages-mars.com/image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mars - Earth Comparison</td>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                         0                1                2\n",
       "0  Mars - Earth Comparison             Mars            Earth\n",
       "1                Diameter:         6,779 km        12,742 km\n",
       "2                    Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "3                   Moons:                2                1\n",
       "4       Distance from Sun:   227,943,824 km   149,598,262 km"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Description</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Mars            Earth\n",
       "Description                                              \n",
       "Mars - Earth Comparison             Mars            Earth\n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km\n",
       "Length of Year:           687 Earth days      365.24 days\n",
       "Temperature:                -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns=['Description','Mars','Earth']\n",
    "df.set_index('Description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th>Description</th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Mars - Earth Comparison</th>\\n      <td>Mars</td>\\n      <td>Earth</td>\\n    </tr>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg</td>\\n      <td>5.97 × 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n      <td>-88 to 58°C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df. to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://marshemispheres.com/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "#creating list to hold images\n",
    "hemisphere_image_urls = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<html lang=\"en\"><head>\n",
       "<meta content=\"text/html; charset=utf-8\" http-equiv=\"Content-Type\"/>\n",
       "<link href=\"css/jquery-ui.css\" rel=\"stylesheet\" type=\"text/css\"/>\n",
       "<title>Astropedia Search Results | GUSS Astrogeology Science Center</title>\n",
       "<meta content=\"GUSS Astrogeology Science Center Astropedia search results.\" name=\"description\"/>\n",
       "<meta content=\"GUSS,Astrogeology Science Center,Cartography,Geology,Space,Geological Survey,Mapping\" name=\"keywords\"/>\n",
       "<meta content=\"IE=edge\" http-equiv=\"X-UA-Compatible\"/>\n",
       "<meta content=\"width=device-width, initial-scale=1, maximum-scale=1\" name=\"viewport\"/>\n",
       "<link href=\"css/main.css\" media=\"screen\" rel=\"stylesheet\"/>\n",
       "<link href=\"css/print.css\" media=\"print\" rel=\"stylesheet\"/>\n",
       "<link href=\"#\" rel=\"icon\" type=\"image/x-ico\"/>\n",
       "</head>\n",
       "<body id=\"results\">\n",
       "<header>\n",
       "<a href=\"#\" style=\"float:right;margin-top:10px;\" target=\"_blank\">\n",
       "<img alt=\"USGS: Science for a Changing World\" class=\"logo\" height=\"60\" src=\"images/usgs_logo_main_2x.png\"/>\n",
       "</a>\n",
       "<a href=\"#\" style=\"float:right;margin-top:5px;margin-right:20px;\" target=\"_blank\">\n",
       "<img alt=\"NASA\" class=\"logo\" height=\"65\" src=\"images/nasa-logo-web-med.png\"/>\n",
       "</a>\n",
       "</header>\n",
       "<div class=\"wrapper\">\n",
       "<div class=\"container\">\n",
       "<div class=\"widget block bar\">\n",
       "<a href=\"https://astrogeology.usgs.gov/search\" style=\"float:right;text-decoration:none;\">\n",
       "<img alt=\"Astropedia\" src=\"images/astropedia-logo-main.png\" style=\"width:200px;border:none;float:right;\"/>\n",
       "<div style=\"clear:both;font-size:.8em;float:right;color:#888;\">Lunar and Planetary Cartographic Catalog</div>\n",
       "</a>\n",
       "<div style=\"float:left;height:60px;\">\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"full-content\">\n",
       "<section class=\"block\" id=\"results-accordian\">\n",
       "<div class=\"result-list\" data-section=\"product\" id=\"product-section\">\n",
       "<div class=\"accordian\">\n",
       "<h2>Products</h2>\n",
       "<span class=\"count\">4 Results</span>\n",
       "<span class=\"collapse\">Collapse</span>\n",
       "</div>\n",
       "<div class=\"collapsible results\">\n",
       "<div class=\"item\">\n",
       "<a class=\"itemLink product-item\" href=\"cerberus.html\"><img alt=\"Cerberus Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png\"/></a>\n",
       "<div class=\"description\">\n",
       "<a class=\"itemLink product-item\" href=\"cerberus.html\">\n",
       "<h3>Cerberus Hemisphere Enhanced</h3>\n",
       "</a>\n",
       "<span class=\"subtitle\" style=\"float:left\">image/tiff 21 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/>\n",
       "<p>Mosaic of the Cerberus hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of 104 Viking Orbiter images acquired…</p>\n",
       "</div>\n",
       "<!-- end description -->\n",
       "</div>\n",
       "<div class=\"item\">\n",
       "<a class=\"itemLink product-item\" href=\"schiaparelli.html\"><img alt=\"Schiaparelli Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png\"/></a>\n",
       "<div class=\"description\">\n",
       "<a class=\"itemLink product-item\" href=\"schiaparelli.html\">\n",
       "<h3>Schiaparelli Hemisphere Enhanced</h3>\n",
       "</a>\n",
       "<span class=\"subtitle\" style=\"float:left\">image/tiff 35 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/>\n",
       "<p>Mosaic of the Schiaparelli hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The images were acquired in 1980 during early northern…</p>\n",
       "</div>\n",
       "<!-- end description -->\n",
       "</div>\n",
       "<div class=\"item\">\n",
       "<a class=\"itemLink product-item\" href=\"syrtis.html\"><img alt=\"Syrtis Major Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png\"/></a>\n",
       "<div class=\"description\">\n",
       "<a class=\"itemLink product-item\" href=\"syrtis.html\">\n",
       "<h3>Syrtis Major Hemisphere Enhanced</h3>\n",
       "</a>\n",
       "<span class=\"subtitle\" style=\"float:left\">image/tiff 25 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/>\n",
       "<p>Mosaic of the Syrtis Major hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of about 100 red and violet…</p>\n",
       "</div>\n",
       "<!-- end description -->\n",
       "</div>\n",
       "<div class=\"item\">\n",
       "<a class=\"itemLink product-item\" href=\"valles.html\"><img alt=\"Valles Marineris Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png\"/></a>\n",
       "<div class=\"description\">\n",
       "<a class=\"itemLink product-item\" href=\"valles.html\">\n",
       "<h3>Valles Marineris Hemisphere Enhanced</h3>\n",
       "</a>\n",
       "<span class=\"subtitle\" style=\"float:left\">image/tiff 27 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/>\n",
       "<p>Mosaic of the Valles Marineris hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The distance is 2500 kilometers from the surface of…</p>\n",
       "</div>\n",
       "<!-- end description -->\n",
       "</div>\n",
       "</div>\n",
       "<!-- end this-section -->\n",
       "</div>\n",
       "</section>\n",
       "</div>\n",
       "<div class=\"navigation clear\" style=\"display: none;\">\n",
       "<a class=\"itemLink product-item\" href=\"#\" onclick=\"showMain()\">\n",
       "<h3>Back</h3>\n",
       "</a>\n",
       "</div>\n",
       "</div>\n",
       "<footer>\n",
       "<div class=\"left\">\n",
       "<a href=\"#\">Search</a> |\n",
       "               <a href=\"#\">About</a> |\n",
       "               <a href=\"#\">Contact</a>\n",
       "</div>\n",
       "<div class=\"right\">\n",
       "<a href=\"#\">GUSS Science Center</a>\n",
       "</div>\n",
       "</footer>\n",
       "</div>\n",
       "<div class=\"page-background\" style=\"\n",
       "         background:url('./images/mars.jpg');\n",
       "         filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(\n",
       "         src='./images/mars.jpg', sizingMethod='scale');\n",
       "         \"></div>\n",
       "<script type=\"text/javascript\">\n",
       "         var baseUrl = \"\";\n",
       "\n",
       "\n",
       "\n",
       "      </script>\n",
       "<script src=\"js/jquery.min.js\" type=\"text/javascript\"></script>\n",
       "<script src=\"js/jquery-ui.min.js\" type=\"text/javascript\"></script>\n",
       "<script src=\"js/general.js\" type=\"text/javascript\"></script>\n",
       "</body></html>"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "html = browser.html\n",
    "img_soup = bs(html, 'html.parser')\n",
    "img_soup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "# 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    "html = browser.html\n",
    "img_soup = bs(html,'html.parser')\n",
    "results = img_soup.find_all('div', class_='description')\n",
    "\n",
    "for item in results:\n",
    "    # gets image title and adds title to list\n",
    "    title = item.find('h3').text\n",
    "    \n",
    "    # gets href, appends it to URL base, visits new page\n",
    "    href = item.find('a')['href']\n",
    "    img_url = url + href\n",
    "    browser.visit(img_url)\n",
    "    new_html = browser.html\n",
    "    new_soup = bs(new_html, 'html.parser')\n",
    "\n",
    "    # Gets image url from new page\n",
    "    image_tag = new_soup.find('div', class_ = 'downloads')\n",
    "    jpg_url = image_tag.find('a')['href']\n",
    "    jpg_url = url + jpg_url\n",
    "    \n",
    "    # Adds items to hemisphere_image_urls\n",
    "    temp_dict = dict({'img_url': jpg_url, 'title': title})\n",
    "    hemisphere_image_urls.append(temp_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'img_url': 'https://marshemispheres.com/images/full.jpg',\n",
       "  'title': 'Cerberus Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg',\n",
       "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg',\n",
       "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg',\n",
       "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4. Print the list that holds the dictionary of each image url and title.\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Quit the browser\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:root] *",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
