import tkinter as tk
from tkinter import messagebox
import random

gui_flashcards = [
    {
        "question": "On an annual basis, the United States consumes a diverse, yet uneven, group of energy resources, ~51% of which consists of fossil fuels (coal, oil, and natural gas).",
        "choices": ["True", "False"],
        "correct": {"False"}
    },
    {
        "question": "Power is defined a rate of energy use, production, or conversion.  Which of the following units is an example of a unit of power?",
        "choices": ["Watts (W)", "British Thermal Unit (Btu)", "Kilocalorie (kcal)", "Joules (J)"],
        "correct": {"Watts (W)"}
    },
    {
        "question": "Which of the following statements explains why the U.S. continues to import crude oil from Canada at a rate of ~4 million barrels per day?",
        "choices": [
            "All of the answer options combined correctly explain why the U.S. imports Canadian oil.",
            "Many U.S. refineries were designed to process heavy crude oil.",
            "Oil imports from Canada are primarily heavy crudes.",
            "The majority of oil produced in the U.S. is light crude oil.",
            "Idle refineries do not produce operational profits."
        ],
        "correct": {"All of the answer options combined correctly explain why the U.S. imports Canadian oil."}
    },
    {
        "question": "Current financial investments in future fossil fuel production may lead to an economic crisis, commonly called the ________ , should fossil fuel resources be left untouched to prevent further climate change.",
        "choices": ["Gross Domestic Product", "EROI", "2008 Great Recession", "Carbon Bubble"],
        "correct": {"Carbon Bubble"}
    },
    {
        "question": "Which of the following units describes the largest quantity of energy?",
        "choices": ["Quad (Q)", "British Thermal Unit (Btu)", "Kilocalorie (kcal)", "Joule (J)"],
        "correct": {"Quad (Q)"}
    },
    {
        "question": "Why can one not compare solar and wind power to fossil fuels in terms of energy density?",
        "choices": [
            "The area occupied by a solar or wind installation can be co-opted for other purposes.",
            "No mass is consumed when using solar or wind power to produce electricity.",
            "Solar and wind power are intermittent unlike fossil fuels.",
            "EROI values of wind and solar are below the economic threshold of 7."
        ],
        "correct": {"No mass is consumed when using solar or wind power to produce electricity."}
    },
    {
        "question": "Producing electricity at a power plant involves a serial conversion of various types of energy.  Which of the following energy conversions has the lowest efficiency?",
        "choices": [
            "Thermal energy to Chemical energy",
            "Chemical energy to thermal energy",
            "Mechanical energy to electrical energy",
            "Thermal energy to mechanical energy"
        ],
        "correct": {"Thermal energy to mechanical energy"}
    },
    {
        "question": "Recall our discussion of the power density of a solar photovoltaic array.  The efficiency of a solar array is the proportion of solar energy that is converted to electricity.\n\nIf an area of land receives solar energy at a rate of 200 W/m2 and the efficiency of the solar array is 15%, what is the expected power density of the solar array?",
        "choices": ["1333 W/m2", "30 W/m2", "The power density cannot be calculated with the provided information.", "3000 W/m2"],
        "correct": {"30 W/m2"}
    },
    {
        "question": "Which of the following regions exhibits the highest level of energy poverty?",
        "choices": ["Sub-Saharan Africa", "North Africa", "North America", "Latin America"],
        "correct": {"Sub-Saharan Africa"}
    },
    {
        "question": "Which of the following statements is FALSE about the different types of coal mining?",
        "choices": [
            "Underground coal mining techniques vary in the proportion of coal extracted.",
            "Strip mine reclamation involves returning surface topography to its approximate original contours.",
            "Longwall mining involves placing overburden in adjacent stream valleys.",
            "Fugitive methane emissions occur at both underground and surface coal mines"
        ],
        "correct": {"Longwall mining involves placing overburden in adjacent stream valleys."}
    },
    {
        "question": "Low concentrations of metals, such as selenium, in surface waters can lead to toxicity symptoms in aquatic organisms, especially offspring, via ________.",
        "choices": ["metal excretion rates exceeding metal intake rates", "mine remediation", "bioaccumulation", "biomagnification"],
        "correct": {"bioaccumulation"}
    },
    {
        "question": "Read the following statement very carefully and determine whether it is True or False.\n\nParticles of bottom ash, a type of coal ash, are often used in cement production because they are nearly spherical, have an almost pure silica composition, and are small in size.",
        "choices": ["True", "False"],
        "correct": {"False"}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nSulfate (SO42-) concentrations in surface water can be used as a proxy for extent of coal mining in a watershed due to the ________ that occurs at both surface and underground coal mines.",
        "choices": ["fugitive methane", "bioaccumulation", "acid mine drainage", "selenium discharge"],
        "correct": {"acid mine drainage"}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nIn coal mining regions, acid mine drainage is the result of __________.",
        "choices": [
            "Oxidation of sulfur-bearing organic matter in the coal.",
            "Acids used to extract coal",
            "Pulverized limestone used as rock dust in underground mines.",
            "Oxidation of sulfur-bearing minerals (pyrite) in coal"
        ],
        "correct": {"Oxidation of sulfur-bearing minerals (pyrite) in coal"}
    },
    {
        "question": "What happens to the overburden at surface coal mines, like open pit mines and mountaintop removal mines?",
        "choices": [
            "The overburden at both types of surface mines is typically used to back fill mining pits and return the landscape to its approximate original contours (i.e., original topography).",
            "The overburden at a mountaintop removal mine is typically used to back fill mining pits and return the landscape to its approximate original contours (i.e., original topography). The overburden at an open pit mine is placed in adjacent stream valleys, resulting in a lower relief landscape.",
            "The overburden at an open pit mine is typically used to back fill mining pits and return the landscape to its approximate original contours (i.e., original topography). The overburden at a mountain top removal mine is placed in adjacent stream valleys, resulting in a lower relief landscape.",
            "The overburden at both types of surface mines is placed in adjacent stream valleys, resulting in a lower relief landscape."
        ],
        "correct": {"The overburden at an open pit mine is typically used to back fill mining pits and return the landscape to its approximate original contours (i.e., original topography). The overburden at a mountain top removal mine is placed in adjacent stream valleys, resulting in a lower relief landscape."}
    },
    {
        "question": "Which of the following terms is defined as the connectivity between open spaces in rock?",
        "choices": ["Resistivity", "Porosity", "Permeability", "Migration pathway"],
        "correct": {"Permeability"}
    },
    {
        "question": "Casing and cementing an oil production well prevents __________ . (Select all that apply)",
        "choices": [
            "flooding of seawater into the deep, hydrocarbon-producing areas of the borehole.",
            "inward collapse of the borehole.",
            "drilling mud from coming into contact with reservoir rocks during a pressure integrity test.",
            "contamination of aquifers (i.e., bodies of groundwater) that are perforated by the well."
        ],
        "correct": {"inward collapse of the borehole.", "contamination of aquifers (i.e., bodies of groundwater) that are perforated by the well."}
    },
    {
        "question": "The temperature and pressure conditions between 6 and 9 km depth that produce hydrocarbons are termed the _______.",
        "choices": ["Kerogen Window", "Oil Window", "Graphite Window", "Natural Gas Window"],
        "correct": {"Natural Gas Window"}
    },
        {
        "question": "Which of the following causes the majority of ocean contamination incidents during the upstream stage of the hydrocarbon life-cycle (i.e., exploration and production)?",
        "choices": [
            "Uncontrolled release of pressure at wells (aka blowouts)",
            "Collisions between oil tankers.",
            "Catastrophic failure of storage tanks on drill rigs.",
            "Faults created by the extraction process."
        ],
        "correct": {"Uncontrolled release of pressure at wells (aka blowouts)"}
    },
    {
        "question": "Read the following statement very carefully and determine if it is true or false.\n\nThe application of bacteria, along with nitrogen- and phosphorous-based fertilizers, to oil spills in marine environments is thought to increase the biological breakdown of the hydrocarbons.",
        "choices": ["True", "False"],
        "correct": {"True"}
    },
    {
        "question": "Which of the following statement are true about the response to the Deepwater Horizon spill?",
        "choices": [
            "All of the answer options are correct.",
            "The National Environmental Policy Act was signed into law as a consequence.",
            "Only 25% (1.25 million barrels) of the oil released was removed from the ocean and coastal environments.",
            "The Blowout Preventer (BOP) operated perfectly despite the failed cement and casing at the Macondo Well."
        ],
        "correct": {"Only 25% (1.25 million barrels) of the oil released was removed from the ocean and coastal environments."}
    },
    {
        "question": "What is produced water (aka production water or formation water)?",
        "choices": [
            "Potable groundwater produced during initial stages of drilling hydrocarbon wells",
            "A solvent added to drilling mud to enhance production of hydrocarbons.",
            "Naturally-occurring, salt-rich water in subsurface rock strata",
            "Naturally-occurring freshwater withdrawn from the ground when extracting oil and natural gas."
        ],
        "correct": {"Naturally-occurring, salt-rich water in subsurface rock strata"}
    },
    {
        "question": "Choose the option that best completes the following sentence:\n\nAnthropogenic oil spills have a detrimental impact on wildlife and ecosystems by ________ .",
        "choices": [
            "releasing carcinogenic and immunosuppressive substances into aquatic and terrestrial environments.",
            "exposing marine organisms to low salinity produced water, forcing them into physiological shock.",
            "causing \"blooms\" of photosynthetic organisms that quickly create low-oxygen water when they decompose.",
            "All of the answer options are correct."
        ],
        "correct": {"releasing carcinogenic and immunosuppressive substances into aquatic and terrestrial environments."}
    },
    {
        "question": "What is the largest contributor to hydrocarbons “leaked” into the oceans?",
        "choices": [
            "Production well blowouts",
            "End-user consumption",
            "Oil tanker accidents",
            "Natural seeps"
        ],
        "correct": {"Natural seeps"}
    },
    {
        "question": "Read the following statement very carefully and determine if it is true or false.\n\nCommon causes of leaks in crude oil pipelines are internal corrosion and deviated (i.e., un-centered) steel casing.",
        "choices": ["True", "False"],
        "correct": {"False"}
    },
    {
        "question": "What are relief wells in the context of well blowouts?",
        "choices": [
            "Relief wells are drilled to release pore pressure at wastewater injection sites, preventing anthropogenic earthquakes.",
            "Relief wells are drilled to facilitate in situ oil sand extraction in low permeability rock layers.",
            "Relief wells are drilled to intercept and seal a production well that has lost pressure control.",
            "Relief wells are drilled to facilitate enhanced oil recovery at convention oil and natural gas fields."
        ],
        "correct": {"Relief wells are drilled to intercept and seal a production well that has lost pressure control."}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nThe process of hydraulic fracturing or “fracking” in a shale play is necessary to produce gas/oil because __________ .",
        "choices": [
            "The porosity and permeability of the shale play are low.",
            "The pores are not well connected in the shale play. Fracturing it will connect the pores and increase permeability.",
            "All of the answer options are correct.",
            "The artificially-produced fracture system will close unless proppants are used."
        ],
        "correct": {"All of the answer options are correct."}
    },
    {
        "question": "Which of the following is NOT a type of additive in frack fluids?",
        "choices": [
            "Guar gum",
            "Biocides",
            "Phosphorous- and nitrogen-based fertilizers",
            "Acid"
        ],
        "correct": {"Phosphorous- and nitrogen-based fertilizers"}
    },
    {
        "question": "The increase in the number of 3.0 magnitude earthquakes in the U.S. from 21 per year in 2000 to 100+ per year after the year 2000 is coincident with what?",
        "choices": [
            "Development of a midcontinental rift in the New Madrid seismic zone",
            "An increase in wastewater disposal well injections",
            "Growth in underground oil shale mining operations.",
            "Drilling and hydraulic fracturing of horizontal wells."
        ],
        "correct": {"An increase in wastewater disposal well injections"}
    },
    {
        "question": "Which of the following are ways to prevent groundwater contamination by frac fluid, methane, and produced water?",
        "choices": [
            "All of the answer options are correct.",
            "Surveys conducted using historical records and satellite imagery to find abandoned oil and natural gas wells.",
            "Avoidance of subsurface faults using information from seismic surveys.",
            "Pressure integrity tests of well casings and cement."
        ],
        "correct": {"All of the answer options are correct."}
    },
    {
        "question": "Choose the option that best completes the following sentence:\n\nThe fracking water cycle has 5 general stages including ________ .",
        "choices": [
            "Water acquisition and steam production",
            "Chemical mixing and wastewater treatment",
            "Well injection and steam assisted gravity drainage",
            "Brine acquisition and aquifer communication"
        ],
        "correct": {"Chemical mixing and wastewater treatment"}
    },
    {
        "question": "What observations have been made based on data from the three 5.0+ magnitude earthquakes in the Wilzetta oil field, Oklahoma, in 2011?",
        "choices": [
            "None of the aftershocks occurred in the sedimentary layer in which wastewater was injected.",
            "All of the answer options are correct.",
            "Fault movement started more than 2 km from the injection disposal wells.",
            "Pore pressure due to wastewater injection did not completely dissipate over time."
        ],
        "correct": {"Pore pressure due to wastewater injection did not completely dissipate over time."}
    },
        {
        "question": "Which of the following is FALSE about wastewater related to hydrocarbon production via conventional and/or hydraulic fracturing (HF) techniques?",
        "choices": [
            "Municipal wastewater treatment facilities can effectively remove the salt content and naturally-occurring radioactive materials from HF wastewater.",
            "Wastewater from conventional and hydraulic fracturing production can be recycled for secondary phase recovery and future frack treatments (i.e., stimulations).",
            "All of the answer options are true.",
            "Disposal of waste water underground is regulated by the Safe Drinking Water Act"
        ],
        "correct": {"Municipal wastewater treatment facilities can effectively remove the salt content and naturally-occurring radioactive materials from HF wastewater."}
    },
    {
        "question": "According to the Scientific American article entitled \"Drilling for Earthquakes\", the risk of anthropogenic earthquakes, such as those that have occurred in Oklahoma, should immediately decrease once wastewater injection has ceased.",
        "choices": ["True", "False"],
        "correct": {"False"}
    },
    {
        "question": "What is pore pressure?",
        "choices": [
            "the pressure exerted by fluids within the pores of rocks",
            "a measure of the connectivity between pores",
            "the proportion of open space within rocks and volumes of sediment",
            "the pressure exerted on pore fluids by the overlying rock and sediment"
        ],
        "correct": {"the pressure exerted by fluids within the pores of rocks"}
    },
    {
        "question": "Which of the following contributes to the substantial reclamation debt of oil sand operations in Alberta, Canada?",
        "choices": [
            "The higher energy demands of in situ extraction leads to greater deforestation rates.",
            "Mature fine tailings in impoundments can take 30 years or more to settle out of wastewater.",
            "None of the answer options are correct.",
            "Boreal forests in Alberta recover slowly due to high water stress."
        ],
        "correct": {"Mature fine tailings in impoundments can take 30 years or more to settle out of wastewater."}
    },
    {
        "question": "Which of the following options is TRUE regarding the transportation of dilbit crude?",
        "choices": [
            "Companies are required to invest in syncrude upgrading facilities before transporting dilbit by either rail or pipeline.",
            "Spill clean-up is more difficult due to evaporation of volatile diluents and subsequent settling of dense bitumen.",
            "None of the answer options are true.",
            "Shipping by rail is more profitable than transporting dilbit by pipeline."
        ],
        "correct": {"Spill clean-up is more difficult due to evaporation of volatile diluents and subsequent settling of dense bitumen."}
    },
    {
        "question": "Steam assisted gravity drainage (SAGD), a form of in situ oil sand production, was found to generate more carbon dioxide emissions than ex situ bitumen mining.\n\nWhich of the following statements correctly explains the greater carbon emissions of SAGD?",
        "choices": [
            "All of the answer options are correct.",
            "SAGD techniques require large electrical heating elements to be inserted at depths of 75 meters or greater. These electrical heating elements are powered by electricity from gigawatt-capacity coal power plants.",
            "The greater carbon emissions of SAGD are due to the burning of natural gas for steam production. The carbon emissions due to steam production are roughly twice as high as emissions from diesel-fueled mining equipment.",
            "The poor quality of the bitumen recovered from SAGD requires mandatory upgrading to synthetic crude oil, a process that requires 2000 cubic feet of natural gas for every barrel of synthetic crude."
        ],
        "correct": {"The greater carbon emissions of SAGD are due to the burning of natural gas for steam production. The carbon emissions due to steam production are roughly twice as high as emissions from diesel-fueled mining equipment."}
    },
    {
        "question": "Why did the 2010 Kalamazoo River dilbit spill require two phases of clean-up?",
        "choices": [
            "The first phase of the clean-up primarily removed the low-density diluent. A second phase of dredging river sediment was necessary to remove settled, high-density bitumen.",
            "The first phase of the clean-up primarily removed the low-density bitumen. A second phase of dredging river sediment was necessary to remove settled, high-density diluent.",
            "A second, previously undetected rupture was discovered in the Enbridge pipeline.",
            "One of the tank rail cars that did not explode in the accident derailed at a bridge upstream from the primary spill site."
        ],
        "correct": {"The first phase of the clean-up primarily removed the low-density diluent. A second phase of dredging river sediment was necessary to remove settled, high-density bitumen."}
    },
    {
        "question": "What are mature fine tailings in the context of oil sand extraction?",
        "choices": [
            "a mixture of high salinity water, fine-grained sediment, and unrecovered bitumen",
            "the low viscosity bitumen that is produced during in situ extraction",
            "a mixture of high salinity water, fine-grained sediment, and sulfur compounds from acid mine drainage",
            "a mixture of naphtha and natural gas condensates used to dilute bitumen into a crude-like substance"
        ],
        "correct": {"a mixture of high salinity water, fine-grained sediment, and unrecovered bitumen"}
    },
    {
        "question": "Choose the option that completes the following statement.\n\nA geographic area in which _____________  is often described as having low water stress.",
        "choices": [
            "All of the answer options are correct.",
            "the water-oil ratio of conventional and unconventional hydrocarbon production are equal",
            "human activity consumes less than 10% of available water resources",
            "the rates of recycling of hydraulic fracturing wastewater are greater than deep injection rates"
        ],
        "correct": {"human activity consumes less than 10% of available water resources"}
    },
    {
        "question": "Which of the following correctly lists a human or mechanical error that contributed to the Macondo Well blowout and the 2010 Deepwater Horizon spill?",
        "choices": [
            "All of the answer options are correct.",
            "The heavy drilling mud used to create pressure control prior to production was withdrawn from the well too early.",
            "The initial explosion on the Deepwater Horizon bent the production pipe within the blowout preventer (BOP). The ram shear within the BOP cut a gash in the production pipe allowing hydrocarbons to spill at a higher rate.",
            "BP chose to use only 6 casing centralizers instead of the suggested 21. This caused cement around the casing to be thin in some places, creating a weak points where natural gas can escape."
        ],
        "correct": {"All of the answer options are correct."}
    },
    {
        "question": "What is PM2.5?",
        "choices": [
            "Airborne particulate matter that has a diameter between 2.5 and 10 microns.",
            "The lower threshold of pH conditions in acidic soils.",
            "The EPA drinking water standard for peroxyacyl nitrates (2.5 ppt)",
            "Airborne particulate matter that has a diameter less than 2.5 microns."
        ],
        "correct": {"Airborne particulate matter that has a diameter less than 2.5 microns."}
    },
    {
        "question": "Read the following statement carefully and determine whether it is true or false.\n\nCarbon monoxide (CO) results from incomplete combustion of fossil fuels due to lack of sufficient oxygen.",
        "choices": ["True", "False"],
        "correct": {"True"}
    },
    {
        "question": "Read the following statement carefully and determine whether it is true or false.\n\nNOx compounds form when atmospheric nitrogen oxidizes at high temperatures during combustion of fossil fuels.",
        "choices": ["True", "False"],
        "correct": {"True"}
    },
    {
        "question": "Choose the option that best completes the following sentence.\n\nNaturally-occurring  ______ do not have the acid neutralizing capacity to prevent detrimental effects of acid deposition, such as nutrient ______.",
        "choices": [
            "acidic soils; leaching",
            "acidic soils; retention",
            "alkaline soils; depletion",
            "alkaline soils; leaching"
        ],
        "correct": {"acidic soils; leaching"}
    },
    {
        "question": "Choose the option that best completes the following sentence:\n\nPassage of Title IV of 1990 Clean Air Act Amendments was important, because ________ .",
        "choices": [
            "All of the answer options are correct.",
            "it allowed electrical utilities to increase sulfur emissions relative to 1980 emission rates.",
            "It established a non-market-based approach to reducing emissions.",
            "It showed how successfully a cap and trade system combined with new emission reduction technology could work"
        ],
        "correct": {"It showed how successfully a cap and trade system combined with new emission reduction technology could work"}
    },
    {
        "question": "In parts of the country where areas of photochemical smog often occurs, why does the peak concentration of ozone (O3) occur in the afternoon between noon and 3 pm?",
        "choices": [
            "The land breeze (i.e. wind blowing from the land out to the sea) is strongest in the early afternoon.",
            "All of the answer options are correct.",
            "Solar UV radiation is necessary to produce ozone, and the sun is highest on the horizon during the early afternoon.",
            "Primary pollutants from vehicles are emitted predominantly from noon to 3 pm."
        ],
        "correct": {"Solar UV radiation is necessary to produce ozone, and the sun is highest on the horizon during the early afternoon."}
    },
    {
        "question": "Read the following statement carefully and determine whether it is true or false.\n\nData from the Multi-Ethnic Study of Atherosclerosis found that not all components of PM2.5 were associated with an increase in carotid artery thickness (CIMT).  More specifically, exposure to the sulfur and silicon components of PM2.5 exhibited the greatest effect on CIMT.",
        "choices": ["True", "False"],
        "correct": {"False"}
    },
    {
        "question": "Which of the following is a difference between point source and nonpoint source emitters of airborne pollution?",
        "choices": [
            "Primary pollutants from nonpoint source emitters do not produce secondary pollutants.",
            "Nonpoint source emitters are widely distributed while point source emitters are localized.",
            "All of the answer options are correct.",
            "Point source emitters contribute more of every type of airborne pollutant, including CO and NOx compounds, than nonpoint source emitters."
        ],
        "correct": {"Nonpoint source emitters are widely distributed while point source emitters are localized."}
    },
    {
        "question": "Choose the option that best completes the following sentence.\n\nThe historical increase in atmospheric carbon dioxide concentrations is correlated with a large negative excursion in atmospheric carbon isotopes.  This correlation suggests that the major source of historical carbon dioxide emissions is ________ .",
        "choices": [
            "organic carbon",
            "heavy carbon isotopes",
            "none of the answer options are correct",
            "volcanic eruptions"
        ],
        "correct": {"organic carbon"}
    },
    {
        "question": "Read the following statement carefully and determine whether it is true or false.\n\nChanges in the characteristics of severe weather events over long time scales (decades or longer) are evidence of climate change.",
        "choices": ["True", "False"],
        "correct": {"True"}
    },
    {
        "question": "Which of the following is an effect of climate change already happening in Iowa?",
        "choices": [
            "An increase in annual precipitation",
            "An increase in the extent of ice coverage",
            "A shorter growing season",
            "A decrease in flood risk"
        ],
        "correct": {"An increase in annual precipitation"}
    },
    {
        "question": "What is the average emissivity of Earth's surface with respect to solar radiation? \n\nHint:  The Earth's surface encounters incoming solar radiation at a rate of 184 W/m2 and, on average, reflects 12% back into outer space, ",
        "choices": [
            "100% or 1.0",
            "12% or 0.12",
            "93% or 0.93",
            "88% or 0.88"
        ],
        "correct": {"88% or 0.88"}
    },
    {
        "question": "Which of the following explains the gaps in the infrared emission spectrum (i.e., transmissivity spectrum) of the Earth?",
        "choices": [
            "Greenhouse gases, such as water vapor, ozone, and CO2, absorb significant amount of energy at those infrared wavelengths.",
            "Is your spectrometer plugged in? Have you tried turning it off and then on again?",
            "Gaps in the emission spectra indicate infrared wavelengths that are not absorbed by the atmosphere.",
            "Airborne pollutants, such as particulate matter, reflect incoming solar radiation."
        ],
        "correct": {"Greenhouse gases, such as water vapor, ozone, and CO2, absorb significant amount of energy at those infrared wavelengths."}
    },
    {
        "question": "Choose the options that best complete the following statement.\n\nThe Stefan-Boltzmann Radiation Law was used in lecture to test hypotheses concerning the cause of recent global warming.\n\nGenerally speaking, the Stefan-Boltzmann Law describes the relationship between the temperature of an object and the ________.",
        "choices": [
            "proportion of energy transmitted through the object",
            "proportion of energy reflected by the object",
            "the temperature of its atmosphere",
            "rate of energy radiated from the object."
        ],
        "correct": {"rate of energy radiated from the object."}
    },
    {
        "question": "How is modern climate change expected to affect the rate at which carbon dioxide is absorbed by the oceanic carbon reservoir?",
        "choices": [
            "The rate will decrease, because warmer, more buoyant surface water will not readily sink in the deeper ocean.",
            "The rate will decrease, because the deep ocean with soon be saturated in carbon.",
            "The rate will increase, because warmer, more buoyant surface water will readily sink into the deeper ocean.",
            "None of the answer options are correct."
        ],
        "correct": {"The rate will decrease, because warmer, more buoyant surface water will not readily sink in the deeper ocean."}
    },
    {
        "question": "What are the 3 major reservoirs of carbon besides the atmosphere?",
        "choices": [
            "Terrestrial plants/soil, the deep ocean, and the lithosphere",
            "Coal, oil, and natural gas",
            "Terrestrial plants/soil, permafrost, and the deep ocean",
            "Terrestrial plants/soil, the MacKenzie River Basin, and the lithosphere"
        ],
        "correct": {"Terrestrial plants/soil, the deep ocean, and the lithosphere"}
    },
    {
        "question": "In the context of ocean fertilization, a form of geoengineering, what is the purpose of seeding the ocean with soluble iron?\n\nChoose the option that best answers this question.",
        "choices": [
            "Iron is a limited nutrient in the ocean. Adding iron will increase the rate of chemical weathering in ocean environments and remove carbon from the atmosphere at a higher rate.",
            "Iron will react rapidly with carbon dissolved in the ocean, creating a highly reflective material as a form of solar radiation management.",
            "Iron prevents the dissolved carbon in the ocean from being oxidized into carbon dioxide.",
            "Iron is a limited nutrient in the ocean. Adding iron may increase photosynthetic productivity and remove carbon from the atmosphere at a higher rate."
        ],
        "correct": {"Iron is a limited nutrient in the ocean. Adding iron may increase photosynthetic productivity and remove carbon from the atmosphere at a higher rate."}
    },
    {
        "question": "What carbon reservoir has the largest capacity for storing atmospheric carbon?",
        "choices": ["The lithosphere", "Permafrost", "Energy crops", "The deep ocean"],
        "correct": {"The lithosphere"}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nAgricultural studies involving greater incorporation of organic carbon into soils reveal a ________ effect, suggesting that the terrestrial carbon reservoir may reach its capacity in the near future.",
        "choices": [
            "carbon antagonistic",
            "soil fertilization",
            "carbon saturation",
            "soil moderation"
        ],
        "correct": {"carbon saturation"}
    },
    {
        "question": "Emissions of some airborne pollutants are reduced during the production or use of biofuels, as compared to gasoline, but not all.\n\nWhich of the following pollutants are NOT reduced when producing and/or using biofuel blends?",
        "choices": ["PM2.5", "NOx compounds", "carbon monoxide", "Sulfur compounds"],
        "correct": {"NOx compounds"}
    },
    {
        "question": "Choose the option that best completes the following statement:\n\nExpanded biofuel production under a RCP4.5 scenario could potentially lead to greater ________ than predicted under RCP8 scenarios.",
        "choices": ["water conservation in the United States", "global surface temperature increase", "variability in precipitation", "water stress in the United States"],
        "correct": {"water stress in the United States"}
    },
    {
        "question": "Choose the option that best completes the following sentence:\n\nIn the past decade, the growth in US renewable electrical capacity is primarily due to expansion of ________.",
        "choices": ["biofuel production", "hydropower", "wind and solar power", "geothermal energy"],
        "correct": {"wind and solar power"}
    },
    {
        "question": "Choose the option that best completes the following statement:\n\nEvaporation of leachate to prevent _______ is a beneficial use of burning landfill methane.",
        "choices": ["greenhouse gas emissions", "soil nutrient loss", "release of radioactive waste", "groundwater contamination"],
        "correct": {"groundwater contamination"}
    },
    {
        "question": "Under what circumstances could biofuel production potentially generate a larger carbon footprint than conventional hydrocarbons?",
        "choices": [
            "When nitrogenous fertilizers are used on energy crops in low nutrient soils.",
            "When the energy returned on investment is lower than the 7 threshold.",
            "When water stress is exacerbated in regions that irrigate corn",
            "When natural environments are converted to agricultural land for energy crops."
        ],
        "correct": {"When natural environments are converted to agricultural land for energy crops."}
    },
    {
        "question": "Which of the following describes an advantage of burning municipal solid waste (MSW) to generate electricity?",
        "choices": [
            "It's a carbon neutral process, because only food and agricultural waste are burned.",
            "Only the ash is sent to a landfill. Reducing landfill use by 85%.",
            "The energy density of MSW is greater than coal.",
            "All of the answer options are correct."
        ],
        "correct": {"Only the ash is sent to a landfill. Reducing landfill use by 85%."}
    },
    {
        "question": "What are the primary goals of the Renewable Fuel Standard (RFS)?\n\n(Mark all that apply)",
        "choices": [
            "Reduce U.S. dependence on oil imports",
            "Reduce greenhouse gas emissions relative to traditional gasoline/diesel",
            "Reduce water pollution related to fossil fuel production",
            "Reduce land use change related to fossil fuel production"
        ],
        "correct": {
            "Reduce U.S. dependence on oil imports",
            "Reduce greenhouse gas emissions relative to traditional gasoline/diesel"
        }
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nPassage of the Renewable Fuel Standard led to greater volatility in corn prices and _____________.",
        "choices": [
            "a reduction in agricultural land use change.",
            "greater food insecurity for impoverished communities and nations.",
            "a decrease in biofuel production.",
            "greater imports of corn and corn products into the United States."
        ],
        "correct": {"greater food insecurity for impoverished communities and nations."}
    },
    {
        "question": "Choose the option that best completes the following sentence:\n\nManufacturing of CSP or PV components may incur emissions of carbon dioxide and airborne pollutants, requiring ________ .",
        "choices": [
            "An energy payback time of more than 2 years to offset this environmental debt.",
            "Further regulation of the solar power industry by the EPA",
            "All of the answer options are correct",
            "Additional emission reduction technology, such electrostatic precipitators, at solar arrays"
        ],
        "correct": {"An energy payback time of more than 2 years to offset this environmental debt."}
    },
    {
        "question": "“Not in my backyard” arguments against wind energy are typically based on issues not related to human and environmental health risks, including __________ .",
        "choices": [
            "Fear of eminent domain use",
            "All of the options are correct.",
            "Fear of lower property values",
            "Noise pollution"
        ],
        "correct": {"All of the options are correct."}
    },
    {
        "question": "How does the band gap energy of a semiconductor affect the efficiency of a solar PV panel?",
        "choices": [
            "The spectrum of wavelengths that a solar PV panel can absorb and convert to electricity is constrained by the band gap energy of its semiconductor material.",
            "The concentration ratio at which a solar PV panel operates is constrained by the band gap energy of its semiconductor material.",
            "The storage capability of molten salt is constrained by the band gap energy of its semiconductor material.",
            "The energy density of a solar PV panel is constrained by the band gap energy of its semiconductor material."
        ],
        "correct": {"The spectrum of wavelengths that a solar PV panel can absorb and convert to electricity is constrained by the band gap energy of its semiconductor material."}
    },
    {
        "question": "Read the following statement very carefully and determine if it is true or false.\n\nConcentrated solar power arrays are effectively heat engines, using solar energy to produce steam and generate electricity.",
        "choices": ["True", "False"],
        "correct": {"True"}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nLarge portions of the United States are currently unsuitable for utility-scale wind farms due to  _________ .",
        "choices": [
            "the water stress and the high water demand for cooling wind turbines",
            "them just being too darn pretty for wind turbines",
            "having annual average wind speeds below the 6.4 m/s threshold",
            "the lack of nearby rare earth element mines"
        ],
        "correct": {"having annual average wind speeds below the 6.4 m/s threshold"}
    },
    {
        "question": "Which of the following is TRUE about average irradiance in the context of solar power?",
        "choices": [
            "No utility-scale and commercially-viable solar power plants are present north of 30°N latitude.",
            "Irradiance/insolation vary within an order of magnitude across different latitudes and regional climates",
            "None of the answer options are true.",
            "Peak irradiance/insolation in the northern hemisphere occurs in a latitudinal band centered at 10°N latitude."
        ],
        "correct": {"Irradiance/insolation vary within an order of magnitude across different latitudes and regional climates"}
    },
    {
        "question": "Environmental concerns associated with wind energy include:\n\n(Mark all that apply)",
        "choices": [
            "Wind-powered feral cats",
            "Intermittent wind power production during peak electrical demand",
            "Hazards related to rare earth element mining and processing",
            "Displacement of communities for compressed air storage"
        ],
        "correct": {
            "Intermittent wind power production during peak electrical demand",
            "Hazards related to rare earth element mining and processing"
        }
    },
    {
        "question": "Choose the option or options that correctly complete the following statement.  Mark all that apply.\n\nRare earth elements are notoriously difficult to separate and purify into metals, leading to ____________ .",
        "choices": [
            "significant energy consumption for roasting and electrolysis.",
            "greater rates of wind turbine recycling, especially in the United States.",
            "higher rates of solar photovoltaic arrays being replaced by concentrated solar power techniques.",
            "significant quantities of acidic wastewater due to acidic separation steps."
        ],
        "correct": {
            "significant energy consumption for roasting and electrolysis.",
            "significant quantities of acidic wastewater due to acidic separation steps."
        }
    },
    {
        "question": "What are the general requirements for producing electricity from a geothermal resource?",
        "choices": [
            "Closed water circulation system, heat pump, and source of electricity",
            "Subsurface temperature greater than 90 degrees Celsius, presence of subsurface water, and permeable rocks",
            "Subsurface heat flow in excess of 185 W/m2",
            "Subsurface temperature greater than 150 degrees Celsius, presence of subsurface water, and impermeable rocks"
        ],
        "correct": {"Subsurface temperature greater than 90 degrees Celsius, presence of subsurface water, and permeable rocks"}
    },
    {
        "question": "Why has there been limited development of geothermal energy in the U.S.?",
        "choices": [
            "Lack of adequate geothermal resources in the contiguous 48 states.",
            "The upfront costs of identifying an adequate geothermal resource make geothermal power plants more expensive than natural gas.",
            "A nearly 30-year moratorium on construction due to the Three Mile Island disaster",
            "Insufficient heat flow, especially on the tectonically-active west coast"
        ],
        "correct": {"The upfront costs of identifying an adequate geothermal resource make geothermal power plants more expensive than natural gas."}
    },
    {
        "question": "Why are \"dry steam\" geothermal power plants so rare in the United States?",
        "choices": [
            "Steam utilized at a dry steam plant is produced naturally in the subsurface. There are only two places in the U.S. where this occurs: Yellowstone National Park and the Geysers Area of California.",
            "The early expansion of dry steam geothermal plants induced devastating earthquakes in South Korea. The U.S. has been hesitant to repeat the same mistakes.",
            "The dry steam process requires active volcanism to generate steam. This only occurs in remote places, such as Alaska and Hawaii.",
            "The dry steam process is experimental and requires artificially fracturing subsurface rocks to produce steam."
        ],
        "correct": {"Steam utilized at a dry steam plant is produced naturally in the subsurface. There are only two places in the U.S. where this occurs: Yellowstone National Park and the Geysers Area of California."}
    },
    {
        "question": "What are benefits of adding Li-ion battery storage to an electrical grid?\n\n(Mark all that apply)",
        "choices": [
            "There are no environmental sustainability issues with battery storage.",
            "Battery storage provides greater reliability during times of peak electrical demand.",
            "Battery storage using Li-ion technology is a net-producer of electricity when combined with renewables, like solar and wind.",
            "Battery storage reduces load variability at power plants and associated maintenance costs."
        ],
        "correct": {
            "Battery storage provides greater reliability during times of peak electrical demand.",
            "Battery storage reduces load variability at power plants and associated maintenance costs."
        }
    },
    {
        "question": "Which of the following options describes an environmental sustainability issue related to lithium extraction?",
        "choices": [
            "Lithium extraction using evaporation ponds increases rates of acid mine drainage into freshwater rivers.",
            "Brine extraction in the Atacama decreases recharge of freshwater aquifers and supply of freshwater to rivers.",
            "Lithium extracted from oil and natural gas wastewater leads to lower thermal tolerance for batteries and greater risks of explosions.",
            "Lithium extraction using evaporation ponds involves \"sulfuric acid roasting\" which produces an acidic waste fluid."
        ],
        "correct": {"Brine extraction in the Atacama decreases recharge of freshwater aquifers and supply of freshwater to rivers."}
    },
    {
        "question": "Choose the options that best completes the following statement.\n\nThe advantage of a binary geothermal power plant is _______________ .",
        "choices": [
            "the relative higher efficiency related to the dry steam or flash steam processes.",
            "that there is no need to purchase or maintain a working fluid for steam production.",
            "that there is greater sustainability of the subsurface fluid reservoir.",
            "the ability to generate electricity without steam production."
        ],
        "correct": {"that there is greater sustainability of the subsurface fluid reservoir."}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nDeveloping enhanced geothermal systems may lead to anthropogenic earthquakes due to ________________ .",
        "choices": [
            "an artificial increase in pore pressure within the geothermal reservoir.",
            "inadvertently triggering a massive release of magma to the surface.",
            "higher rates of thermal contraction and surface subsidence.",
            "a reduction in pore pressure once the naturally-occurring steam has been released."
        ],
        "correct": {"an artificial increase in pore pressure within the geothermal reservoir."}
    },
    {
        "question": "What is one reason that hydroelectric dams and their associated reservoirs have a finite lifespan?",
        "choices": [
            "Too many fish gumming up the turbines",
            "Reduced capacity of the reservoir due to accumulation of sediment behind the dam",
            "Higher electrical loads due usage of pumped storage",
            "Constant water erosion upstream of the dam"
        ],
        "correct": {"Reduced capacity of the reservoir due to accumulation of sediment behind the dam"}
    },
    {
        "question": "Besides the physical barrier imposed by a dam, how does hydropower detrimentally \"segment\" watersheds and aquatic ecosystems?",
        "choices": [
            "Salinity tends to be lower in the upstream reservoir than elsewhere along river.",
            "Water temperature tends to be lower in the upstream reservoir than elsewhere along river.",
            "Salinity tends to be higher in the upstream reservoir than elsewhere along river.",
            "Sediment erosion tends to be higher in the upstream reservoir than elsewhere along river."
        ],
        "correct": {"Salinity tends to be higher in the upstream reservoir than elsewhere along river."}
    },
    {
        "question": "Read the following statement carefully and determine if it is True or False.\n\nIn the context of hydroelectric power, pumped storage makes generation of electricity more economical by reducing variability in electrical load at a power plant.",
        "choices": ["True", "False"],
        "correct": {"True"}
    },
    {
        "question": "What are the benefits of impoundment hydropower?\n\n(Mark all that apply)",
        "choices": [
            "The impoundment, or reservoir, provides a source of freshwater, especially in arid regions.",
            "Land use change can be minimized in areas of low topographic relief.",
            "Impoundment hydropower is a highly efficient process for generating renewable electricity.",
            "The impoundment and dam provide a means of flood control for downstream communities."
        ],
        "correct": {
            "The impoundment, or reservoir, provides a source of freshwater, especially in arid regions.",
            "Impoundment hydropower is a highly efficient process for generating renewable electricity.",
            "The impoundment and dam provide a means of flood control for downstream communities."
        }
    }
]
exam2_flashcards = [
            {
        "question": "Which of the following causes the majority of ocean contamination incidents during the upstream stage of the hydrocarbon life-cycle (i.e., exploration and production)?",
        "choices": [
            "Uncontrolled release of pressure at wells (aka blowouts)",
            "Collisions between oil tankers.",
            "Catastrophic failure of storage tanks on drill rigs.",
            "Faults created by the extraction process."
        ],
        "correct": {"Uncontrolled release of pressure at wells (aka blowouts)"}
    },
    # Question 24
{
    "question": "What is a \"well blowout\"?",
    "choices": [
        "The final stage of well completion at a hydraulic fracturing site during which flowback water returns to the surface.",
        "A process similar to the \"top kill\" procedure used to regain pressure control at a leaking oil well.",
        "An uncontrolled release of hydrocarbons due to loss of pressure control at the production site.",
        "None of the answer options are correct."
    ],
    "correct": {"An uncontrolled release of hydrocarbons due to loss of pressure control at the production site."}
},

# Question 25
{
    "question": "Read the following statement very carefully and determine if it true or false.\n\nThe horizontal length of a hydraulic fracturing (HF) well typically varies from 1-3 kilometers whereas the artificial fracture network only extends 30-100 meters from the HF well.",
    "choices": ["True", "False"],
    "correct": {"True"}
},
# Question 27
{
    "question": "Which of the following options is not a common frac fluid additive?",
    "choices": [
        "Corrosion inhibitors to ensure casing integrity.",
        "Surfactants that reduce the surface tension between hydrocarbons, water, and rock particles.",
        "Gels that thicken frac fluid to better transport proppant.",
        "Acids used to slowly dissolve proppant particles."
    ],
    "correct": {"Acids used to slowly dissolve proppant particles."}
},
# Question 28 (corrected)
{
    "question": "Boreal forests are being cleared for expansion of oil sand mining in Alberta, Canada.\n\nWhich of the following statements correctly describes an environmental impact of clearing boreal forests?",
    "choices": [
        "Boreal forests are major freshwater reservoirs. Clearing the boreal forests may potentially decrease water resources, exacerbating water stress in the Alberta province.",
        "Boreal forests occupy naturally-acidic soils. Clearing the boreal forests will exacerbate loss of biodiversity due to acid deposition.",
        "All of the answer options are correct.",
        "Boreal forests are major carbon reservoirs. Clearing the boreal forests may potentially release a large quantity of carbon into the atmosphere, exacerbating climate change."
    ],
    "correct": {"Boreal forests are major carbon reservoirs. Clearing the boreal forests may potentially release a large quantity of carbon into the atmosphere, exacerbating climate change."}
},
# Question 30
{
    "question": "Choose the option that best completes the following statement.\n\nA study combining satellite imagery, direct sampling, and oceanographic modelling indicates that oil from the Deepwater Horizon Disaster may have spread _____________________",
    "choices": [
        "only via surface water currents and was not entrained in deep water currents.",
        "All of the answer options are correct.",
        "only in the Gulf of Mexico without entering the greater Atlantic Ocean.",
        "beyond closed fisheries and contaminated other areas of the Gulf of Mexico."
    ],
    "correct": {"beyond closed fisheries and contaminated other areas of the Gulf of Mexico."}
},

# Question 31
{
    "question": "In the context of hydraulic fracturing, what is the purpose of proppant?",
    "choices": [
        "None of the answer options are correct.",
        "Proppant decreases the viscosity of hydrocarbons, increasing the production rate.",
        "Proppant prevents internal corrosion of casing in production wells.",
        "Proppant ensures the network of fractures remains open, allowing flow of hydrocarbons."
    ],
    "correct": {"Proppant ensures the network of fractures remains open, allowing flow of hydrocarbons."}
},

# Question 32
{
    "question": "Domestic drinking water wells in northeastern Pennsylvania were contaminated with methane in 2007-2009, coincident with the expansion of hydraulic fracturing operations in the area.\n\nWhich of the following statements explains the link between methane contamination and hydraulic fracturing (HF) in this context?",
    "choices": [
        "All of the answer options are correct.",
        "Drilling of HF wells disturbed shallow sources of methane. Then, improperly abandoned wells acted as migration pathways that connected the methane source and drinkable groundwater.",
        "Short term storage of flowback and produced water at HF production sites leaked downward into drinkable groundwater sources.",
        "The artificial network of fractures created by HF techniques extended vertically for 1-10 kilometers connecting the source rock and the drinkable groundwater."
    ],
    "correct": {"Drilling of HF wells disturbed shallow sources of methane. Then, improperly abandoned wells acted as migration pathways that connected the methane source and drinkable groundwater."}
},
# Question 34
{
    "question": "Scientific studies indicate that hydraulic fracturing (HF) operations near Pavillion, WY, did contaminate groundwater resources during the injection or well stimulation stage of production.\n\nWhat component of these HF operations most likely allowed the contamination to occur?\n\n(select all that apply)",
    "choices": [
        "Cement and steel casing at the HF wells did not extend to the production zone in the oil field.",
        "The induced fracture pattern extended several kilometers upward into the shallow groundwater resources.",
        "Well injection occurred in the same geologic formation as the groundwater resources only 200 feet below the deepest groundwater well.",
        "Abandoned oil wells served as artificial pathways for hydrocarbons to travel into groundwater resources."
    ],
    "correct": {
        "Cement and steel casing at the HF wells did not extend to the production zone in the oil field.",
        "Well injection occurred in the same geologic formation as the groundwater resources only 200 feet below the deepest groundwater well.",
        "Abandoned oil wells served as artificial pathways for hydrocarbons to travel into groundwater resources."
    }
},

# Question 35
{
    "question": "Choose the option that best completes the following statement.\n\nIngestion of hydrocarbon poses a long-term health risk to organisms due to the fact that _______________ .",
    "choices": [
        "some hydrocarbons are lipid-soluble and have long residence times within tissues.",
        "light hydrocarbons easily evaporate into the atmosphere.",
        "dense hydrocarbons are preserved in sediment at the sea floor.",
        "some hydrocarbons are water-soluble and are quickly excreted."
    ],
    "correct": {"some hydrocarbons are lipid-soluble and have long residence times within tissues."}
},
# Corrected Question 37
{
    "question": "What observations have been made based on data from the three 5.0+ magnitude earthquakes in the Wilzetta oil field, Oklahoma, in 2011?",
    "choices": [
        "All of the answer options are correct.",
        "Pore pressure due to wastewater injection did not completely dissipate over time as expected.",
        "None of the aftershocks occurred in the sedimentary layer in which wastewater was injected.",
        "Fault movement started more than 2 km from the injection disposal wells."
    ],
    "correct": {"Pore pressure due to wastewater injection did not completely dissipate over time as expected."}
},
# Corrected Question 38
{
    "question": "Which of the following is TRUE regarding the transportation of dilbit crude?",
    "choices": [
        "None of the answer options are true.",
        "Dilbit crude is more frequently transported to refineries designed to process light, sweet conventional crude oil.",
        "Bitumen is denser than water and is consequently easier to clean up after a pipeline spill than conventional, light crude oil.",
        "Companies do not need to invest in syncrude upgrading facilities before transporting dilbit by either rail or pipeline."
    ],
    "correct": {"Companies do not need to invest in syncrude upgrading facilities before transporting dilbit by either rail or pipeline."}
},
# Question 39
{
    "question": "Which of the following statements is/are TRUE about differences between natural hydrocarbon seeps and anthropogenic hydrocarbon \"spills\"?\n\n(Mark all that apply)",
    "choices": [
        "Over long time periods (years to decades), anthropogenic spills contribute more hydrocarbons to marine environments than natural seeps.",
        "Over long time periods (years to decades), natural seeps contribute more hydrocarbons to marine environments than anthropogenic spills.",
        "Rates of hydrocarbon release at natural seeps are 100-1000x slower than rates during anthropogenic spills.",
        "Rates of hydrocarbon release during anthropogenic spills are 100-1000x slower than rates at natural seeps."
    ],
    "correct": {
        "Over long time periods (years to decades), natural seeps contribute more hydrocarbons to marine environments than anthropogenic spills.",
        "Rates of hydrocarbon release at natural seeps are 100-1000x slower than rates during anthropogenic spills."
    }
},
# Question 41
{
    "question": "Which of the following statements best describes why Canada's oil sand deposits are unconventional hydrocarbons?",
    "choices": [
        "There may have been an incomplete trap and seal geometry that trapped the high density hydrocarbons but allowed the low density hydrocarbons to seep upwards.",
        "During oil sand extraction, hydrocarbons are removed directly from the source rock. There are migration pathways, reservoir rocks, or trap/seals associated with oil sand deposits.",
        "Oil sand deposits need to be artificially fractured in order to increase permeability in the reservoir rock.",
        "All of the answer options are correct."
    ],
    "correct": {"There may have been an incomplete trap and seal geometry that trapped the high density hydrocarbons but allowed the low density hydrocarbons to seep upwards."}
},
    {
        "question": "Choose the option that best completes the following statement:\n\nCorexit, the dispersant chemical used in the Deepwater Horizon clean up, was found to be moderately toxic, because it facilitated  __________ the tissue of aquatic organisms.",
        "choices": [
            "the removal of nutrients and oxygen from",
            "an increase in deliciousness and human consumption of",
            "the absorption of small hydrocarbon particles into",
            "the precipitation of iron hydroxides within"
        ],
        "correct": {"the absorption of small hydrocarbon particles into"}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nOil and natural gas production produces billions of liters of wastewater each year.  Treating this wastewater at municipal and industrial wastewater treatment plants was determined to be insufficient because ________ .",
        "choices": [
            "the effluent from the treatment plants had a high concentration of volatile hydrocarbons.",
            "the effluent from the treatment plants deposited naturally-occurring radioactive material in stream sediment.",
            "the effluent from the treatment plants had a high concentration of sulfuric acid.",
            "the effluent from the treatment plants had a salt content that was abnormally low, even for freshwater ecosystems."
        ],
        "correct": {"the effluent from the treatment plants deposited naturally-occurring radioactive material in stream sediment."}
    },
    {
        "question": "What are mature fine tailings in the context of oil sand extraction?",
        "choices": [
            "the low viscosity bitumen that is produced during in situ extraction",
            "a mixture of high salinity water, fine-grained sediment, and sulfur compounds from acid mine drainage",
            "a mixture of naphtha and natural gas condensates used to dilute bitumen into a crude-like substance",
            "a mixture of high salinity water, fine-grained sediment, and unrecovered bitumen"
        ],
        "correct": {"a mixture of high salinity water, fine-grained sediment, and unrecovered bitumen"}
    },
    {
        "question": "The majority of cases of hydrocarbon contamination in marine environments during oil exploration and extraction can be attributed to what?",
        "choices": [
            "Loss of pressure control at the well or borehole (i.e., well blowout).",
            "Corroded pipelines that transport crude oil and natural gas.",
            "The stimulation stage of offshore hydraulic fracturing.",
            "Catastrophic failure of the trap and seal geometry."
        ],
        "correct": {"Loss of pressure control at the well or borehole (i.e., well blowout)."}
    },
    {
        "question": "When hydrocarbons \"leak\" into the ocean, either at natural seeps or due to anthropogenic spills, what is the expected fate of the heavy, tar-like hydrocarbons?",
        "choices": [
            "The heavy hydrocarbons will evaporate into the atmosphere within 24 hours.",
            "The heavy hydrocarbons will be incorporated into the sediment on the seafloor.",
            "Bacteria will consume the heavy hydrocarbons that float within the water column.",
            "None of the answer options are correct."
        ],
        "correct": {"The heavy hydrocarbons will be incorporated into the sediment on the seafloor."}
    },
    {
        "question": "During the enhanced oil recovery process (EOR), what is the purpose of pumping carbon dioxide, steam, and liquid water into a conventional oil reservoir?",
        "choices": [
            "The carbon dioxide and steam drive the remaining oil into a production well. The liquid water is pumped in as a way to dispose of wastewater.",
            "The carbon dioxide and steam lower the viscosity and surface tension of the remaining oil in the reservoir. The liquid water drives the oil into a production well.",
            "The carbon dioxide and steam converts the oil to natural gas. The liquid water drives the natural gas into a production well.",
            "None of the answer options are correct."
        ],
        "correct": {"The carbon dioxide and steam lower the viscosity and surface tension of the remaining oil in the reservoir. The liquid water drives the oil into a production well."}
    },
{
    "question": "Why is the energy returned on investment (EROI) lower for synthetic crude oil than conventional light, sweet crude oil?",
    "choices": [
        "The waste water to oil ratio for oil sand extraction can be higher than 20, requiring greater energy expenditures to properly dispose of the waste water.",
        "The use of carbon capture technology during bitumen upgrading is more energy intensive than a conventional crude oil refinery.",
        "Upgrading bitumen into a synthetic crude oil requires hydrogenation and consumption of large volumes of natural gas.",
        "All of the answer options are correct."
    ],
    "correct": {"Upgrading bitumen into a synthetic crude oil requires hydrogenation and consumption of large volumes of natural gas."}
},
{
    "question": "How does water demand for oil sand production compare with water demand during conventional oil production?",
    "choices": [
        "The water-oil ratio (WOR) for ex situ and in situ extraction methods may be equal to or exceed the conventional oil WOR range.",
        "The water-oil ratio (WOR) for ex situ and in situ extraction methods is on the low end of the conventional oil WOR range.",
        "The water-oil ratio (WOR) for ex situ extraction is on the low end of the conventional oil WOR range.  The in situ extraction WOR may be equal to or higher than the conventional WOR range.",
        "The water-oil ratio (WOR) for in situ extraction is on the low end of the conventional oil WOR range.  The ex situ extraction WOR may be equal to or exceed the conventional WOR range."
    ],
    "correct": {"The water-oil ratio (WOR) for in situ extraction is on the low end of the conventional oil WOR range.  The ex situ extraction WOR may be equal to or exceed the conventional WOR range."}
},
    {
        "question": "Choose the option that best completes the following sentence:\n\nAnthropogenic oil spills have a detrimental impact on wildlife and ecosystems by ________ .",
        "choices": [
            "All of the answer options are correct.",
            "causing phytoplankton blooms and subsequent anoxia through input of nitrogen and phosphorous nutrients.",
            "causing inflammation of tissues (short-term exposure) and damage to organ systems (long-term exposure).",
            "increasing photosynthetic productivity at the expense of chemosynthetic productivity."
        ],
        "correct": {"causing inflammation of tissues (short-term exposure) and damage to organ systems (long-term exposure)."}
    },
    {
        "question": "Which of the following is TRUE about wastewater related to conventional and unconventional hydrocarbon production?",
        "choices": [
            "Wastewater from conventional and hydraulic fracturing production can be recycled for secondary phase recovery and future frack treatments (i.e., stimulations).",
            "All of the answer options are true.",
            "Produced water can have a salt content that greatly exceeds that of seawater.",
            "Disposal of waste water underground is regulated by the Safe Drinking Water Act"
        ],
        "correct": {"All of the answer options are true."}
    },
    {
        "question": "What is the largest contributor to hydrocarbons “leaked” into the oceans?",
        "choices": [
            "End-user oil consumption",
            "Natural seeps",
            "Deepwater Horizon disaster",
            "Oil tanker accidents"
        ],
        "correct": {"Natural seeps"}
    },
    {
        "question": "Choose the option that best completes the following sentence:\n\nAreas in which human activities use a significant amount of available water are called ________ .",
        "choices": [
            "Watersheds",
            "Water stressed areas",
            "Aquatic amusement parks",
            "Aquicludes"
        ],
        "correct": {"Water stressed areas"}
    },
    {
        "question": "Oil and other hydrocarbons can leak into marine environments during production and transportation of the hydrocarbons.\n\nWhat is the goal of the human response or mitigation to spills in marine environments?\n\n(Select all that apply)",
        "choices": [
            "Remove hydrocarbons that have settled onto the seafloor.",
            "Remove hydrocarbons at the ocean surface and prevent them from reaching shore.",
            "Stop the leak of hydrocarbons into the marine environment (e.g., use of relief wells).",
            "Prevent the decomposition of hydrocarbons by microbial life."
        ],
        "correct": {
            "Remove hydrocarbons at the ocean surface and prevent them from reaching shore.",
            "Stop the leak of hydrocarbons into the marine environment (e.g., use of relief wells)."
        }
    },
    {
    "type": "free_response",
    "question": "Evaluate the following statement:\n\n\"When considering production over the entire life spans of conventional and unconventional (hydraulically fractured) oil wells, production at the unconventional well will likely require more water (i.e., be more water intensive).\"\n\nIs this statement true, false, or incomplete? Explain your reasoning.",
    "answer": "This is incomplete because although over the entire lifespan of conventional oil production uses more water with EROI than hydraulically fractured oil production, conventional oil production that doesn't utilize EROI uses less water than unconventional oil wells. Therefore, if the statement specified whether EROI was being utilized, we could determine a complete answer. However in this case, we cannot since conventional oil techniques with EROI use more oil than unconventional oil wells and conventional oil wells without EROI use less."
},
{
    "type": "free_response",
    "question": "A common way to dispose of wastewater generated during hydrocarbon production is to inject the wastewater deep underground.\n\n1. Explain how wastewater injections near faults can induce earthquakes. (3 points)\n2. Why do earthquakes not occur immediately after each injection? (1 point)",
    "answer": "Wastewater injections increase pore pressure at the fault and consequently decrease friction at the fault. Lower friction means that a lower amount of stress is necessary to cause an earthquake. Pore pressure dissipates after each injection but does not return to its previous value. This small net increase in pore pressure requires time to reach the critical pore pressure threshold to induce an earthquake."
},
{
    "type": "free_response",
    "question": "Extracting oil and natural gas from a shale play (i.e., a thermally-mature source rock deep in the subsurface) poses unique problems that cannot be solved using conventional production techniques.\n\nWhat are these problems (at least 3), and how are they solved during hydraulic fracturing operations?",
    "answer": "Three problems with a shale play: 1) horizontal orientation, 2) low permeability, and 3) high confining pressure. Horizontal drilling solves problem 1. Frac fluid stimulation solves problem 2 by forming artificial cracks and permeability. Proppant solves problem 3 by keeping the cracks open."
},
    {
        "question": "Read the following statement very carefully and determine if it is true or false.\n\nThe application of bacteria, along with nitrogen- and phosphorous-based fertilizers, to oil spills in marine environments is thought to increase the biological breakdown of the hydrocarbons.",
        "choices": ["True", "False"],
        "correct": {"True"}
    },
    {
        "question": "Which of the following statement are true about the response to the Deepwater Horizon spill?",
        "choices": [
            "All of the answer options are correct.",
            "The National Environmental Policy Act was signed into law as a consequence.",
            "Only 25% (1.25 million barrels) of the oil released was removed from the ocean and coastal environments.",
            "The Blowout Preventer (BOP) operated perfectly despite the failed cement and casing at the Macondo Well."
        ],
        "correct": {"Only 25% (1.25 million barrels) of the oil released was removed from the ocean and coastal environments."}
    },
    {
        "question": "What is produced water (aka production water or formation water)?",
        "choices": [
            "Potable groundwater produced during initial stages of drilling hydrocarbon wells",
            "A solvent added to drilling mud to enhance production of hydrocarbons.",
            "Naturally-occurring, salt-rich water in subsurface rock strata",
            "Naturally-occurring freshwater withdrawn from the ground when extracting oil and natural gas."
        ],
        "correct": {"Naturally-occurring, salt-rich water in subsurface rock strata"}
    },
    {
        "question": "Choose the option that best completes the following sentence:\n\nAnthropogenic oil spills have a detrimental impact on wildlife and ecosystems by ________ .",
        "choices": [
            "releasing carcinogenic and immunosuppressive substances into aquatic and terrestrial environments.",
            "exposing marine organisms to low salinity produced water, forcing them into physiological shock.",
            "causing \"blooms\" of photosynthetic organisms that quickly create low-oxygen water when they decompose.",
            "All of the answer options are correct."
        ],
        "correct": {"releasing carcinogenic and immunosuppressive substances into aquatic and terrestrial environments."}
    },
    {
        "question": "What is the largest contributor to hydrocarbons “leaked” into the oceans?",
        "choices": [
            "Production well blowouts",
            "End-user consumption",
            "Oil tanker accidents",
            "Natural seeps"
        ],
        "correct": {"Natural seeps"}
    },
    {
        "question": "Read the following statement very carefully and determine if it is true or false.\n\nCommon causes of leaks in crude oil pipelines are internal corrosion and deviated (i.e., un-centered) steel casing.",
        "choices": ["True", "False"],
        "correct": {"False"}
    },
    {
        "question": "What are relief wells in the context of well blowouts?",
        "choices": [
            "Relief wells are drilled to release pore pressure at wastewater injection sites, preventing anthropogenic earthquakes.",
            "Relief wells are drilled to facilitate in situ oil sand extraction in low permeability rock layers.",
            "Relief wells are drilled to intercept and seal a production well that has lost pressure control.",
            "Relief wells are drilled to facilitate enhanced oil recovery at convention oil and natural gas fields."
        ],
        "correct": {"Relief wells are drilled to intercept and seal a production well that has lost pressure control."}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nThe process of hydraulic fracturing or “fracking” in a shale play is necessary to produce gas/oil because __________ .",
        "choices": [
            "The porosity and permeability of the shale play are low.",
            "The pores are not well connected in the shale play. Fracturing it will connect the pores and increase permeability.",
            "All of the answer options are correct.",
            "The artificially-produced fracture system will close unless proppants are used."
        ],
        "correct": {"All of the answer options are correct."}
    },
    {
        "question": "Which of the following is NOT a type of additive in frack fluids?",
        "choices": [
            "Guar gum",
            "Biocides",
            "Phosphorous- and nitrogen-based fertilizers",
            "Acid"
        ],
        "correct": {"Phosphorous- and nitrogen-based fertilizers"}
    },
    {
        "question": "The increase in the number of 3.0 magnitude earthquakes in the U.S. from 21 per year in 2000 to 100+ per year after the year 2000 is coincident with what?",
        "choices": [
            "Development of a midcontinental rift in the New Madrid seismic zone",
            "An increase in wastewater disposal well injections",
            "Growth in underground oil shale mining operations.",
            "Drilling and hydraulic fracturing of horizontal wells."
        ],
        "correct": {"An increase in wastewater disposal well injections"}
    },
    {
        "question": "Which of the following are ways to prevent groundwater contamination by frac fluid, methane, and produced water?",
        "choices": [
            "All of the answer options are correct.",
            "Surveys conducted using historical records and satellite imagery to find abandoned oil and natural gas wells.",
            "Avoidance of subsurface faults using information from seismic surveys.",
            "Pressure integrity tests of well casings and cement."
        ],
        "correct": {"All of the answer options are correct."}
    },
    {
        "question": "Choose the option that best completes the following sentence:\n\nThe fracking water cycle has 5 general stages including ________ .",
        "choices": [
            "Water acquisition and steam production",
            "Chemical mixing and wastewater treatment",
            "Well injection and steam assisted gravity drainage",
            "Brine acquisition and aquifer communication"
        ],
        "correct": {"Chemical mixing and wastewater treatment"}
    },
    {
        "question": "What observations have been made based on data from the three 5.0+ magnitude earthquakes in the Wilzetta oil field, Oklahoma, in 2011?",
        "choices": [
            "None of the aftershocks occurred in the sedimentary layer in which wastewater was injected.",
            "All of the answer options are correct.",
            "Fault movement started more than 2 km from the injection disposal wells.",
            "Pore pressure due to wastewater injection did not completely dissipate over time."
        ],
        "correct": {"Pore pressure due to wastewater injection did not completely dissipate over time."}
    },
        {
        "question": "Which of the following is FALSE about wastewater related to hydrocarbon production via conventional and/or hydraulic fracturing (HF) techniques?",
        "choices": [
            "Municipal wastewater treatment facilities can effectively remove the salt content and naturally-occurring radioactive materials from HF wastewater.",
            "Wastewater from conventional and hydraulic fracturing production can be recycled for secondary phase recovery and future frack treatments (i.e., stimulations).",
            "All of the answer options are true.",
            "Disposal of waste water underground is regulated by the Safe Drinking Water Act"
        ],
        "correct": {"Municipal wastewater treatment facilities can effectively remove the salt content and naturally-occurring radioactive materials from HF wastewater."}
    },
    {
        "question": "According to the Scientific American article entitled \"Drilling for Earthquakes\", the risk of anthropogenic earthquakes, such as those that have occurred in Oklahoma, should immediately decrease once wastewater injection has ceased.",
        "choices": ["True", "False"],
        "correct": {"False"}
    },
    {
        "question": "What is pore pressure?",
        "choices": [
            "the pressure exerted by fluids within the pores of rocks",
            "a measure of the connectivity between pores",
            "the proportion of open space within rocks and volumes of sediment",
            "the pressure exerted on pore fluids by the overlying rock and sediment"
        ],
        "correct": {"the pressure exerted by fluids within the pores of rocks"}
    },
    {
        "question": "Which of the following contributes to the substantial reclamation debt of oil sand operations in Alberta, Canada?",
        "choices": [
            "The higher energy demands of in situ extraction leads to greater deforestation rates.",
            "Mature fine tailings in impoundments can take 30 years or more to settle out of wastewater.",
            "None of the answer options are correct.",
            "Boreal forests in Alberta recover slowly due to high water stress."
        ],
        "correct": {"Mature fine tailings in impoundments can take 30 years or more to settle out of wastewater."}
    },
    {
        "question": "Which of the following options is TRUE regarding the transportation of dilbit crude?",
        "choices": [
            "Companies are required to invest in syncrude upgrading facilities before transporting dilbit by either rail or pipeline.",
            "Spill clean-up is more difficult due to evaporation of volatile diluents and subsequent settling of dense bitumen.",
            "None of the answer options are true.",
            "Shipping by rail is more profitable than transporting dilbit by pipeline."
        ],
        "correct": {"Spill clean-up is more difficult due to evaporation of volatile diluents and subsequent settling of dense bitumen."}
    },
    {
        "question": "Steam assisted gravity drainage (SAGD), a form of in situ oil sand production, was found to generate more carbon dioxide emissions than ex situ bitumen mining.\n\nWhich of the following statements correctly explains the greater carbon emissions of SAGD?",
        "choices": [
            "All of the answer options are correct.",
            "SAGD techniques require large electrical heating elements to be inserted at depths of 75 meters or greater. These electrical heating elements are powered by electricity from gigawatt-capacity coal power plants.",
            "The greater carbon emissions of SAGD are due to the burning of natural gas for steam production. The carbon emissions due to steam production are roughly twice as high as emissions from diesel-fueled mining equipment.",
            "The poor quality of the bitumen recovered from SAGD requires mandatory upgrading to synthetic crude oil, a process that requires 2000 cubic feet of natural gas for every barrel of synthetic crude."
        ],
        "correct": {"The greater carbon emissions of SAGD are due to the burning of natural gas for steam production. The carbon emissions due to steam production are roughly twice as high as emissions from diesel-fueled mining equipment."}
    },
    {
        "question": "Why did the 2010 Kalamazoo River dilbit spill require two phases of clean-up?",
        "choices": [
            "The first phase of the clean-up primarily removed the low-density diluent. A second phase of dredging river sediment was necessary to remove settled, high-density bitumen.",
            "The first phase of the clean-up primarily removed the low-density bitumen. A second phase of dredging river sediment was necessary to remove settled, high-density diluent.",
            "A second, previously undetected rupture was discovered in the Enbridge pipeline.",
            "One of the tank rail cars that did not explode in the accident derailed at a bridge upstream from the primary spill site."
        ],
        "correct": {"The first phase of the clean-up primarily removed the low-density diluent. A second phase of dredging river sediment was necessary to remove settled, high-density bitumen."}
    },
    {
        "question": "Choose the option that completes the following statement.\n\nA geographic area in which _____________  is often described as having low water stress.",
        "choices": [
            "All of the answer options are correct.",
            "the water-oil ratio of conventional and unconventional hydrocarbon production are equal",
            "human activity consumes less than 10% of available water resources",
            "the rates of recycling of hydraulic fracturing wastewater are greater than deep injection rates"
        ],
        "correct": {"human activity consumes less than 10% of available water resources"}
    },
    {
        "question": "Which of the following correctly lists a human or mechanical error that contributed to the Macondo Well blowout and the 2010 Deepwater Horizon spill?",
        "choices": [
            "All of the answer options are correct.",
            "The heavy drilling mud used to create pressure control prior to production was withdrawn from the well too early.",
            "The initial explosion on the Deepwater Horizon bent the production pipe within the blowout preventer (BOP). The ram shear within the BOP cut a gash in the production pipe allowing hydrocarbons to spill at a higher rate.",
            "BP chose to use only 6 casing centralizers instead of the suggested 21. This caused cement around the casing to be thin in some places, creating a weak points where natural gas can escape."
        ],
        "correct": {"All of the answer options are correct."}
    }
]
exam3_flashcards = [
    {
        "question": "What is PM2.5?",
        "choices": [
            "Airborne particulate matter that has a diameter between 2.5 and 10 microns.",
            "The lower threshold of pH conditions in acidic soils.",
            "The EPA drinking water standard for peroxyacyl nitrates (2.5 ppt)",
            "Airborne particulate matter that has a diameter less than 2.5 microns."
        ],
        "correct": {"Airborne particulate matter that has a diameter less than 2.5 microns."}
    },
    {
    "question": "How did the moderator at the Chernobyl Nuclear Power Plant contribute to the release of radioactive material during the disaster?",
    "choices": [
        "All of the answer options are correct.",
        "The water moderator created a hydrogen explosion, sending radioactive steam into local environments.",
        "The graphite moderator ignited, sending a plume of radioactive material high into the atmosphere.",
        "The graphite moderator failed to absorb excess neutrons, creating an uncontrolled chain reaction when the cooling system failed."
    ],
    "correct": {"The graphite moderator ignited, sending a plume of radioactive material high into the atmosphere."}
},
    {
        "question": "Which of the following correctly describes an advantage of the Yucca Mountain repository for long-term storage of spent nuclear fuel?",
        "choices": [
            "Risk management at the repository includes a graphite moderator.",
            "The repository is positioned 1000 feet below the surface but 1000 feet above sources of groundwater.",
            "The repository was constructed in very permeable rock, allowing rapid flow of groundwater.",
            "None of the answer options are correct."
        ],
        "correct": {"The repository is positioned 1000 feet below the surface but 1000 feet above sources of groundwater."}
    },
    {
        "question": "Read the following statement very carefully and determine whether it is true or false.\n\nCarbon monoxide (CO) results from incomplete combustion of fossil fuels due to presence of excess oxygen.",
        "choices": ["True", "False"],
        "correct": {"False"}
    },
    {
        "question": "What was an impact of the Three Mile Island disaster of 1979?",
        "choices": [
            "rapid adoption of graphite reactors worldwide",
            "millions of gallons of radioactive sea water",
            "a nearly 30 year moratorium on construction of new nuclear power plants",
            "the global population exposed to the equivalent of 3 extra weeks of background radiation"
        ],
        "correct": {"a nearly 30 year moratorium on construction of new nuclear power plants"}
    },
    {
        "question": "Choose the option that best completes the following statement:\n\nEnhanced chemical weathering using olivine minerals may involve __________.",
        "choices": [
            "Releasing pulverized olivine in the ocean to react with dissolved CO2.",
            "Pumping CO2-enriched solutions down into subsurface olivine-bearing rocks.",
            "All of the options are correct.",
            "Expanding current olivine mining efforts by 12,500 times."
        ],
        "correct": {"All of the options are correct."}
    },

    {
        "question": "What is a land breeze in the context of photochemical smog?",
        "choices": [
            "A wind current flowing from land to the adjacent ocean that occurs during the evening. The land breeze often prevents airborne pollution from concentrating over coastal cities.",
            "It's a sarcastic term often used to describe the lack of wind during morning rush hour in land-locked cities.",
            "A wind current flowing from the ocean to the adjacent coast that occurs during the morning. The land breeze often concentrates airborne pollution over coastal cities.",
            "A wind current flowing from land to the adjacent ocean that occurs during the evening. The land breeze often concentrates airborne pollution over coastal cities."
        ],
        "correct": {"A wind current flowing from land to the adjacent ocean that occurs during the evening. The land breeze often concentrates airborne pollution over coastal cities."}
    },
    {
        "question": "Spent nuclear fuel (i.e., nuclear waste) in the United States is stored in two stages. Spent fuel rods are temporarily stored in ______ and then transferred to ______.",
        "choices": [
            "cooling pools until they sufficiently decrease in temperature and radioactivity and then transferred to dry casks",
            "dry casks and then transferred to reprocessing facilities",
            "cooling towers and then transferred to underground bunkers",
            "cooling ponds and then transferred to graphite moderators"
        ],
        "correct": {"cooling pools until they sufficiently decrease in temperature and radioactivity and then transferred to dry casks"}
    },
    {
    "question": "Choose the options that best complete the following statement.\n\nUnder geoengineering, examples of solar radiation management and carbon cycle management, respectively, are ______ and ______.",
    "choices": [
        "diminished reflectivity and carbon burial",
        "cloud thinning and afforestation",
        "increased reflectivity and ocean fertilization",
        "diminished reflectivity and ocean fertilization"
    ],
    "correct": {"increased reflectivity and ocean fertilization"}
},
 {
        "question": "Which of the following is not one of the four ideal physical conditions for photochemical smog to develop in an urban area?",
        "choices": [
            "numerous cloud-free days",
            "many non-point source emitters (e.g., road vehicles)",
            "adjacent highlands that block wind currents",
            "low temperature contrast between land and adjacent bodies of water"
        ],
        "correct": {"low temperature contrast between land and adjacent bodies of water"}
    },
    {
        "question": "Which of the following options correctly explains why more progress has been made in reducing sulfuric acid deposition relative to nitric acid deposition?",
        "choices": [
            "A large proportion of sulfur emissions are derived from point source emitters, like power plants. The Clean Air Act Amendments were more effective at reducing emissions from point source emitters than non-point source emitters of NOx compounds.",
            "No specific targets were set by the Clean Air Act Amendments regarding sulfuric acid deposition.",
            "A large proportion of sulfur emissions are derived from non-point source emitters, like vehicles and agriculture. The Clean Air Act Amendments were more effective at reducing emissions from non-point source emitters than common point source emitters of NOx compounds.",
            "The implemented cap-and-trade system imposed on power plants and other point source emitters failed."
        ],
        "correct": {"A large proportion of sulfur emissions are derived from point source emitters, like power plants. The Clean Air Act Amendments were more effective at reducing emissions from point source emitters than non-point source emitters of NOx compounds."}
    },
    {
    "question": "Choose the options that best complete the following statement:\n\nIn the context of photochemical smog, if the ____ is lower than the rate at which a mass of polluted air _______, the polluted air will stop rising and stay concentrated over a city.",
    "choices": [
        "ozone production rate is lower than the rate at which a mass of polluted air gains heat with altitude",
        "atmospheric lapse rate is lower than the rate at which a mass of polluted air loses heat with altitude",
        "sea breeze velocity is lower than the rate at which a mass of polluted air develops secondary pollutants",
        "rate of incoming solar radiation is lower than the rate at which a mass of polluted air develops NOx compounds"
    ],
    "correct": {
        "atmospheric lapse rate is lower than the rate at which a mass of polluted air loses heat with altitude"
    }
},
    {
        "question": "Read the following statement carefully and determine if it is true or false.\n\nIn one of our lectures, we used a simple two layer model of the Earth to test the hypothesis that modern global warming is due to an enhanced greenhouse effect. The hypothesis was supported by the observation that the stratosphere is warming at the same rate as the lower troposphere.",
        "choices": ["True", "False"],
        "correct": {"False"}
    },
     {
        "question": "Which of the following describes a decision made during construction of the Fukushima Daiichi power plant that made it more susceptible to tsunamis?",
        "choices": [
            "Local seismic hazard maps were ignored, resulting in construction that over-compensated for future earthquakes.",
            "The natural seawall was reduced in elevation to facilitate ocean delivery of heavy equipment and prefab modules.",
            "The natural seawall was raised to a higher elevation to provide access to seawater for the coolant system.",
            "Specifications for the artificial seawall were based on inaccurate stone markers scattered throughout the Fukushima prefecture."
        ],
        "correct": {"The natural seawall was reduced in elevation to facilitate ocean delivery of heavy equipment and prefab modules."}
    },
    {
        "question": "Results from open-air experiments suggest that the combined effect of higher temperatures and higher concentrations of atmospheric carbon dioxide will ____________.",
        "choices": [
            "exacerbate soil nutrient leaching",
            "result in increases of above-ground and below-ground biomass",
            "result in a decrease in soil respiration rates",
            "none of the answer options are correct"
        ],
        "correct": {"result in increases of above-ground and below-ground biomass"}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nExposure to acid deposition, and subsequent _________, causes conifers, like the red spruce, to be ________.",
        "choices": [
            "leaching of calcium from needles; more susceptible to frost damage and infections",
            "increase in nitrogen availability; more likely to grow rapidly",
            "oxidation of lignin in bark; better protected against pests",
            "removal of iron from soil; better equipped for photosynthesis"
        ],
        "correct": {"leaching of calcium from needles; more susceptible to frost damage and infections"}
    },
    {
        "question": "Which of the following correctly describes a process through which carbon is removed from the atmosphere and stored in the lithosphere carbon reservoir?",
        "choices": [
            "Volcanic eruptions release carbon dioxide, sulfur dioxide, and other gases into the atmosphere.",
            "Carbon-bearing sediment on the seafloor is thrust up onto continents due to tectonic forces.",
            "Precipitation with dissolved carbonic acid chemically weathers silicate minerals exposed at the surface.",
            "Precipitation with dissolved silicic acid chemically weathers silicate minerals exposed at the surface."
        ],
        "correct": {"Precipitation with dissolved carbonic acid chemically weathers silicate minerals exposed at the surface."}
    },
    {
    "question": "Choose the options that best complete the following statement.\n\nUnder current and future climate change, _________ water in high latitude oceans will _________, decreasing the transport of carbon into the deep ocean reservoir.",
    "choices": [
        "cool; increase chemical weathering rates",
        "cooler; strengthen ocean convection currents",
        "warmer; increase chemical weathering rates",
        "warmer; weaken ocean convection currents"
    ],
    "correct": {"warmer; weaken ocean convection currents"}
},
 {
        "question": "Which of the following correctly lists a fossil fuel-derived airborne pollutant and its corresponding impact on human health?",
        "choices": [
            "Carbon monoxide; atherosclerosis and other cardiovascular disease",
            "PM2.5; binds to blood hemoglobin preventing uptake of oxygen",
            "NOx compounds; atherosclerosis",
            "Carbon monoxide; binds to blood hemoglobin preventing uptake of oxygen"
        ],
        "correct": {"Carbon monoxide; binds to blood hemoglobin preventing uptake of oxygen"}
    },
    {
        "question": "Read the following statement carefully and determine whether it is true or false.\n\nCarbon monoxide (CO) results from incomplete combustion of fossil fuels due to lack of sufficient oxygen.",
        "choices": ["True", "False"],
        "correct": {"True"}
    },
    {
        "question": "Read the following statement carefully and determine whether it is true or false.\n\nNOx compounds form when atmospheric nitrogen oxidizes at high temperatures during combustion of fossil fuels.",
        "choices": ["True", "False"],
        "correct": {"True"}
    },
    {
        "question": "Choose the option that best completes the following sentence.\n\nNaturally-occurring  ______ do not have the acid neutralizing capacity to prevent detrimental effects of acid deposition, such as nutrient ______.",
        "choices": [
            "acidic soils; leaching",
            "acidic soils; retention",
            "alkaline soils; depletion",
            "alkaline soils; leaching"
        ],
        "correct": {"acidic soils; leaching"}
    },
    {
        "question": "Choose the option that best completes the following sentence:\n\nPassage of Title IV of 1990 Clean Air Act Amendments was important, because ________ .",
        "choices": [
            "All of the answer options are correct.",
            "it allowed electrical utilities to increase sulfur emissions relative to 1980 emission rates.",
            "It established a non-market-based approach to reducing emissions.",
            "It showed how successfully a cap and trade system combined with new emission reduction technology could work"
        ],
        "correct": {"It showed how successfully a cap and trade system combined with new emission reduction technology could work"}
    },
    {
        "question": "In parts of the country where areas of photochemical smog often occurs, why does the peak concentration of ozone (O3) occur in the afternoon between noon and 3 pm?",
        "choices": [
            "The land breeze (i.e. wind blowing from the land out to the sea) is strongest in the early afternoon.",
            "All of the answer options are correct.",
            "Solar UV radiation is necessary to produce ozone, and the sun is highest on the horizon during the early afternoon.",
            "Primary pollutants from vehicles are emitted predominantly from noon to 3 pm."
        ],
        "correct": {"Solar UV radiation is necessary to produce ozone, and the sun is highest on the horizon during the early afternoon."}
    },
    {
        "question": "Read the following statement carefully and determine whether it is true or false.\n\nData from the Multi-Ethnic Study of Atherosclerosis found that not all components of PM2.5 were associated with an increase in carotid artery thickness (CIMT).  More specifically, exposure to the sulfur and silicon components of PM2.5 exhibited the greatest effect on CIMT.",
        "choices": ["True", "False"],
        "correct": {"False"}
    },
    {
        "question": "Which of the following is a difference between point source and nonpoint source emitters of airborne pollution?",
        "choices": [
            "Primary pollutants from nonpoint source emitters do not produce secondary pollutants.",
            "Nonpoint source emitters are widely distributed while point source emitters are localized.",
            "All of the answer options are correct.",
            "Point source emitters contribute more of every type of airborne pollutant, including CO and NOx compounds, than nonpoint source emitters."
        ],
        "correct": {"Nonpoint source emitters are widely distributed while point source emitters are localized."}
    },
    {
        "question": "Choose the option that best completes the following sentence.\n\nThe historical increase in atmospheric carbon dioxide concentrations is correlated with a large negative excursion in atmospheric carbon isotopes.  This correlation suggests that the major source of historical carbon dioxide emissions is ________ .",
        "choices": [
            "organic carbon",
            "heavy carbon isotopes",
            "none of the answer options are correct",
            "volcanic eruptions"
        ],
        "correct": {"organic carbon"}
    },
    {
        "question": "Read the following statement carefully and determine whether it is true or false.\n\nChanges in the characteristics of severe weather events over long time scales (decades or longer) are evidence of climate change.",
        "choices": ["True", "False"],
        "correct": {"True"}
    },
    {
        "question": "Which of the following is an effect of climate change already happening in Iowa?",
        "choices": [
            "An increase in annual precipitation",
            "An increase in the extent of ice coverage",
            "A shorter growing season",
            "A decrease in flood risk"
        ],
        "correct": {"An increase in annual precipitation"}
    },
    {
        "question": "What is the average emissivity of Earth's surface with respect to solar radiation? \n\nHint:  The Earth's surface encounters incoming solar radiation at a rate of 184 W/m2 and, on average, reflects 12% back into outer space, ",
        "choices": [
            "100% or 1.0",
            "12% or 0.12",
            "93% or 0.93",
            "88% or 0.88"
        ],
        "correct": {"88% or 0.88"}
    },
    {
        "question": "Which of the following explains the gaps in the infrared emission spectrum (i.e., transmissivity spectrum) of the Earth?",
        "choices": [
            "Greenhouse gases, such as water vapor, ozone, and CO2, absorb significant amount of energy at those infrared wavelengths.",
            "Is your spectrometer plugged in? Have you tried turning it off and then on again?",
            "Gaps in the emission spectra indicate infrared wavelengths that are not absorbed by the atmosphere.",
            "Airborne pollutants, such as particulate matter, reflect incoming solar radiation."
        ],
        "correct": {"Greenhouse gases, such as water vapor, ozone, and CO2, absorb significant amount of energy at those infrared wavelengths."}
    },
    {
        "question": "Choose the options that best complete the following statement.\n\nThe Stefan-Boltzmann Radiation Law was used in lecture to test hypotheses concerning the cause of recent global warming.\n\nGenerally speaking, the Stefan-Boltzmann Law describes the relationship between the temperature of an object and the ________.",
        "choices": [
            "proportion of energy transmitted through the object",
            "proportion of energy reflected by the object",
            "the temperature of its atmosphere",
            "rate of energy radiated from the object."
        ],
        "correct": {"rate of energy radiated from the object."}
    },
    {
        "question": "How is modern climate change expected to affect the rate at which carbon dioxide is absorbed by the oceanic carbon reservoir?",
        "choices": [
            "The rate will decrease, because warmer, more buoyant surface water will not readily sink in the deeper ocean.",
            "The rate will decrease, because the deep ocean with soon be saturated in carbon.",
            "The rate will increase, because warmer, more buoyant surface water will readily sink into the deeper ocean.",
            "None of the answer options are correct."
        ],
        "correct": {"The rate will decrease, because warmer, more buoyant surface water will not readily sink in the deeper ocean."}
    },
    {
        "question": "What are the 3 major reservoirs of carbon besides the atmosphere?",
        "choices": [
            "Terrestrial plants/soil, the deep ocean, and the lithosphere",
            "Coal, oil, and natural gas",
            "Terrestrial plants/soil, permafrost, and the deep ocean",
            "Terrestrial plants/soil, the MacKenzie River Basin, and the lithosphere"
        ],
        "correct": {"Terrestrial plants/soil, the deep ocean, and the lithosphere"}
    },
    {
        "question": "In the context of ocean fertilization, a form of geoengineering, what is the purpose of seeding the ocean with soluble iron?\n\nChoose the option that best answers this question.",
        "choices": [
            "Iron is a limited nutrient in the ocean. Adding iron will increase the rate of chemical weathering in ocean environments and remove carbon from the atmosphere at a higher rate.",
            "Iron will react rapidly with carbon dissolved in the ocean, creating a highly reflective material as a form of solar radiation management.",
            "Iron prevents the dissolved carbon in the ocean from being oxidized into carbon dioxide.",
            "Iron is a limited nutrient in the ocean. Adding iron may increase photosynthetic productivity and remove carbon from the atmosphere at a higher rate."
        ],
        "correct": {"Iron is a limited nutrient in the ocean. Adding iron may increase photosynthetic productivity and remove carbon from the atmosphere at a higher rate."}
    },
    {
        "question": "What carbon reservoir has the largest capacity for storing atmospheric carbon?",
        "choices": ["The lithosphere", "Permafrost", "Energy crops", "The deep ocean"],
        "correct": {"The lithosphere"}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nAgricultural studies involving greater incorporation of organic carbon into soils reveal a ________ effect, suggesting that the terrestrial carbon reservoir may reach its capacity in the near future.",
        "choices": [
            "carbon antagonistic",
            "soil fertilization",
            "carbon saturation",
            "soil moderation"
        ],
        "correct": {"carbon saturation"}
    }
]

bioenergy_flashcards = [
    {
        "question": "Emissions of some airborne pollutants are reduced during the production or use of biofuels, as compared to gasoline, but not all.\n\nWhich of the following pollutants are NOT reduced when producing and/or using biofuel blends?",
        "choices": ["PM2.5", "NOx compounds", "carbon monoxide", "Sulfur compounds"],
        "correct": {"NOx compounds"}
    },
    {
        "question": "Choose the option that best completes the following statement:\n\nExpanded biofuel production under a RCP4.5 scenario could potentially lead to greater ________ than predicted under RCP8 scenarios.",
        "choices": ["water conservation in the United States", "global surface temperature increase", "variability in precipitation", "water stress in the United States"],
        "correct": {"water stress in the United States"}
    },
    {
        "question": "Choose the option that best completes the following sentence:\n\nIn the past decade, the growth in US renewable electrical capacity is primarily due to expansion of ________.",
        "choices": ["biofuel production", "hydropower", "wind and solar power", "geothermal energy"],
        "correct": {"wind and solar power"}
    },
    {
        "question": "Choose the option that best completes the following statement:\n\nEvaporation of leachate to prevent _______ is a beneficial use of burning landfill methane.",
        "choices": ["greenhouse gas emissions", "soil nutrient loss", "release of radioactive waste", "groundwater contamination"],
        "correct": {"groundwater contamination"}
    },
    {
        "question": "Under what circumstances could biofuel production potentially generate a larger carbon footprint than conventional hydrocarbons?",
        "choices": [
            "When nitrogenous fertilizers are used on energy crops in low nutrient soils.",
            "When the energy returned on investment is lower than the 7 threshold.",
            "When water stress is exacerbated in regions that irrigate corn",
            "When natural environments are converted to agricultural land for energy crops."
        ],
        "correct": {"When natural environments are converted to agricultural land for energy crops."}
    },
    {
        "question": "Which of the following describes an advantage of burning municipal solid waste (MSW) to generate electricity?",
        "choices": [
            "It's a carbon neutral process, because only food and agricultural waste are burned.",
            "Only the ash is sent to a landfill. Reducing landfill use by 85%.",
            "The energy density of MSW is greater than coal.",
            "All of the answer options are correct."
        ],
        "correct": {"Only the ash is sent to a landfill. Reducing landfill use by 85%."}
    },
    {
        "question": "What are the primary goals of the Renewable Fuel Standard (RFS)?\n\n(Mark all that apply)",
        "choices": [
            "Reduce U.S. dependence on oil imports",
            "Reduce greenhouse gas emissions relative to traditional gasoline/diesel",
            "Reduce water pollution related to fossil fuel production",
            "Reduce land use change related to fossil fuel production"
        ],
        "correct": {
            "Reduce U.S. dependence on oil imports",
            "Reduce greenhouse gas emissions relative to traditional gasoline/diesel"
        }
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nPassage of the Renewable Fuel Standard led to greater volatility in corn prices and _____________.",
        "choices": [
            "a reduction in agricultural land use change.",
            "greater food insecurity for impoverished communities and nations.",
            "a decrease in biofuel production.",
            "greater imports of corn and corn products into the United States."
        ],
        "correct": {"greater food insecurity for impoverished communities and nations."}
    },
    {
        "question": "Choose the option that best completes the following sentence:\n\nManufacturing of CSP or PV components may incur emissions of carbon dioxide and airborne pollutants, requiring ________ .",
        "choices": [
            "An energy payback time of more than 2 years to offset this environmental debt.",
            "Further regulation of the solar power industry by the EPA",
            "All of the answer options are correct",
            "Additional emission reduction technology, such electrostatic precipitators, at solar arrays"
        ],
        "correct": {"An energy payback time of more than 2 years to offset this environmental debt."}
    },
    {
        "question": "“Not in my backyard” arguments against wind energy are typically based on issues not related to human and environmental health risks, including __________ .",
        "choices": [
            "Fear of eminent domain use",
            "All of the options are correct.",
            "Fear of lower property values",
            "Noise pollution"
        ],
        "correct": {"All of the options are correct."}
    },
    {
        "question": "How does the band gap energy of a semiconductor affect the efficiency of a solar PV panel?",
        "choices": [
            "The spectrum of wavelengths that a solar PV panel can absorb and convert to electricity is constrained by the band gap energy of its semiconductor material.",
            "The concentration ratio at which a solar PV panel operates is constrained by the band gap energy of its semiconductor material.",
            "The storage capability of molten salt is constrained by the band gap energy of its semiconductor material.",
            "The energy density of a solar PV panel is constrained by the band gap energy of its semiconductor material."
        ],
        "correct": {"The spectrum of wavelengths that a solar PV panel can absorb and convert to electricity is constrained by the band gap energy of its semiconductor material."}
    },
    {
        "question": "Read the following statement very carefully and determine if it is true or false.\n\nConcentrated solar power arrays are effectively heat engines, using solar energy to produce steam and generate electricity.",
        "choices": ["True", "False"],
        "correct": {"True"}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nLarge portions of the United States are currently unsuitable for utility-scale wind farms due to  _________ .",
        "choices": [
            "the water stress and the high water demand for cooling wind turbines",
            "them just being too darn pretty for wind turbines",
            "having annual average wind speeds below the 6.4 m/s threshold",
            "the lack of nearby rare earth element mines"
        ],
        "correct": {"having annual average wind speeds below the 6.4 m/s threshold"}
    },
    {
        "question": "Which of the following is TRUE about average irradiance in the context of solar power?",
        "choices": [
            "No utility-scale and commercially-viable solar power plants are present north of 30°N latitude.",
            "Irradiance/insolation vary within an order of magnitude across different latitudes and regional climates",
            "None of the answer options are true.",
            "Peak irradiance/insolation in the northern hemisphere occurs in a latitudinal band centered at 10°N latitude."
        ],
        "correct": {"Irradiance/insolation vary within an order of magnitude across different latitudes and regional climates"}
    },
    {
        "question": "Environmental concerns associated with wind energy include:\n\n(Mark all that apply)",
        "choices": [
            "Wind-powered feral cats",
            "Intermittent wind power production during peak electrical demand",
            "Hazards related to rare earth element mining and processing",
            "Displacement of communities for compressed air storage"
        ],
        "correct": {
            "Intermittent wind power production during peak electrical demand",
            "Hazards related to rare earth element mining and processing"
        }
    },
    {
        "question": "Choose the option or options that correctly complete the following statement.  Mark all that apply.\n\nRare earth elements are notoriously difficult to separate and purify into metals, leading to ____________ .",
        "choices": [
            "significant energy consumption for roasting and electrolysis.",
            "greater rates of wind turbine recycling, especially in the United States.",
            "higher rates of solar photovoltaic arrays being replaced by concentrated solar power techniques.",
            "significant quantities of acidic wastewater due to acidic separation steps."
        ],
        "correct": {
            "significant energy consumption for roasting and electrolysis.",
            "significant quantities of acidic wastewater due to acidic separation steps."
        }
    },
    {
        "question": "What are the general requirements for producing electricity from a geothermal resource?",
        "choices": [
            "Closed water circulation system, heat pump, and source of electricity",
            "Subsurface temperature greater than 90 degrees Celsius, presence of subsurface water, and permeable rocks",
            "Subsurface heat flow in excess of 185 W/m2",
            "Subsurface temperature greater than 150 degrees Celsius, presence of subsurface water, and impermeable rocks"
        ],
        "correct": {"Subsurface temperature greater than 90 degrees Celsius, presence of subsurface water, and permeable rocks"}
    },
    {
        "question": "Why has there been limited development of geothermal energy in the U.S.?",
        "choices": [
            "Lack of adequate geothermal resources in the contiguous 48 states.",
            "The upfront costs of identifying an adequate geothermal resource make geothermal power plants more expensive than natural gas.",
            "A nearly 30-year moratorium on construction due to the Three Mile Island disaster",
            "Insufficient heat flow, especially on the tectonically-active west coast"
        ],
        "correct": {"The upfront costs of identifying an adequate geothermal resource make geothermal power plants more expensive than natural gas."}
    },
    {
        "question": "Why are \"dry steam\" geothermal power plants so rare in the United States?",
        "choices": [
            "Steam utilized at a dry steam plant is produced naturally in the subsurface. There are only two places in the U.S. where this occurs: Yellowstone National Park and the Geysers Area of California.",
            "The early expansion of dry steam geothermal plants induced devastating earthquakes in South Korea. The U.S. has been hesitant to repeat the same mistakes.",
            "The dry steam process requires active volcanism to generate steam. This only occurs in remote places, such as Alaska and Hawaii.",
            "The dry steam process is experimental and requires artificially fracturing subsurface rocks to produce steam."
        ],
        "correct": {"Steam utilized at a dry steam plant is produced naturally in the subsurface. There are only two places in the U.S. where this occurs: Yellowstone National Park and the Geysers Area of California."}
    },
    {
        "question": "What are benefits of adding Li-ion battery storage to an electrical grid?\n\n(Mark all that apply)",
        "choices": [
            "There are no environmental sustainability issues with battery storage.",
            "Battery storage provides greater reliability during times of peak electrical demand.",
            "Battery storage using Li-ion technology is a net-producer of electricity when combined with renewables, like solar and wind.",
            "Battery storage reduces load variability at power plants and associated maintenance costs."
        ],
        "correct": {
            "Battery storage provides greater reliability during times of peak electrical demand.",
            "Battery storage reduces load variability at power plants and associated maintenance costs."
        }
    },
    {
        "question": "Which of the following options describes an environmental sustainability issue related to lithium extraction?",
        "choices": [
            "Lithium extraction using evaporation ponds increases rates of acid mine drainage into freshwater rivers.",
            "Brine extraction in the Atacama decreases recharge of freshwater aquifers and supply of freshwater to rivers.",
            "Lithium extracted from oil and natural gas wastewater leads to lower thermal tolerance for batteries and greater risks of explosions.",
            "Lithium extraction using evaporation ponds involves \"sulfuric acid roasting\" which produces an acidic waste fluid."
        ],
        "correct": {"Brine extraction in the Atacama decreases recharge of freshwater aquifers and supply of freshwater to rivers."}
    },
    {
        "question": "Choose the options that best completes the following statement.\n\nThe advantage of a binary geothermal power plant is _______________ .",
        "choices": [
            "the relative higher efficiency related to the dry steam or flash steam processes.",
            "that there is no need to purchase or maintain a working fluid for steam production.",
            "that there is greater sustainability of the subsurface fluid reservoir.",
            "the ability to generate electricity without steam production."
        ],
        "correct": {"that there is greater sustainability of the subsurface fluid reservoir."}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nDeveloping enhanced geothermal systems may lead to anthropogenic earthquakes due to ________________ .",
        "choices": [
            "an artificial increase in pore pressure within the geothermal reservoir.",
            "inadvertently triggering a massive release of magma to the surface.",
            "higher rates of thermal contraction and surface subsidence.",
            "a reduction in pore pressure once the naturally-occurring steam has been released."
        ],
        "correct": {"an artificial increase in pore pressure within the geothermal reservoir."}
    },
    {
        "question": "What is one reason that hydroelectric dams and their associated reservoirs have a finite lifespan?",
        "choices": [
            "Too many fish gumming up the turbines",
            "Reduced capacity of the reservoir due to accumulation of sediment behind the dam",
            "Higher electrical loads due usage of pumped storage",
            "Constant water erosion upstream of the dam"
        ],
        "correct": {"Reduced capacity of the reservoir due to accumulation of sediment behind the dam"}
    },
    {
        "question": "Besides the physical barrier imposed by a dam, how does hydropower detrimentally \"segment\" watersheds and aquatic ecosystems?",
        "choices": [
            "Salinity tends to be lower in the upstream reservoir than elsewhere along river.",
            "Water temperature tends to be lower in the upstream reservoir than elsewhere along river.",
            "Salinity tends to be higher in the upstream reservoir than elsewhere along river.",
            "Sediment erosion tends to be higher in the upstream reservoir than elsewhere along river."
        ],
        "correct": {"Salinity tends to be higher in the upstream reservoir than elsewhere along river."}
    },
    {
        "question": "Read the following statement carefully and determine if it is True or False.\n\nIn the context of hydroelectric power, pumped storage makes generation of electricity more economical by reducing variability in electrical load at a power plant.",
        "choices": ["True", "False"],
        "correct": {"True"}
    },
    {
        "question": "What are the benefits of impoundment hydropower?\n\n(Mark all that apply)",
        "choices": [
            "The impoundment, or reservoir, provides a source of freshwater, especially in arid regions.",
            "Land use change can be minimized in areas of low topographic relief.",
            "Impoundment hydropower is a highly efficient process for generating renewable electricity.",
            "The impoundment and dam provide a means of flood control for downstream communities."
        ],
        "correct": {
            "The impoundment, or reservoir, provides a source of freshwater, especially in arid regions.",
            "Impoundment hydropower is a highly efficient process for generating renewable electricity.",
            "The impoundment and dam provide a means of flood control for downstream communities."
        }
    }
]
exam1_flashcards = [
    {
        "question": "On an annual basis, the United States consumes a diverse, yet uneven, group of energy resources, ~51% of which consists of fossil fuels (coal, oil, and natural gas).",
        "choices": ["True", "False"],
        "correct": {"False"}
    },
    {
        "question": "Power is defined a rate of energy use, production, or conversion.  Which of the following units is an example of a unit of power?",
        "choices": ["Watts (W)", "British Thermal Unit (Btu)", "Kilocalorie (kcal)", "Joules (J)"],
        "correct": {"Watts (W)"}
    },
    {
        "question": "Which of the following statements explains why the U.S. continues to import crude oil from Canada at a rate of ~4 million barrels per day?",
        "choices": [
            "All of the answer options combined correctly explain why the U.S. imports Canadian oil.",
            "Many U.S. refineries were designed to process heavy crude oil.",
            "Oil imports from Canada are primarily heavy crudes.",
            "The majority of oil produced in the U.S. is light crude oil.",
            "Idle refineries do not produce operational profits."
        ],
        "correct": {"All of the answer options combined correctly explain why the U.S. imports Canadian oil."}
    },
    {
        "question": "Current financial investments in future fossil fuel production may lead to an economic crisis, commonly called the ________ , should fossil fuel resources be left untouched to prevent further climate change.",
        "choices": ["Gross Domestic Product", "EROI", "2008 Great Recession", "Carbon Bubble"],
        "correct": {"Carbon Bubble"}
    },
    {
        "question": "Which of the following units describes the largest quantity of energy?",
        "choices": ["Quad (Q)", "British Thermal Unit (Btu)", "Kilocalorie (kcal)", "Joule (J)"],
        "correct": {"Quad (Q)"}
    },
    {
        "question": "Why can one not compare solar and wind power to fossil fuels in terms of energy density?",
        "choices": [
            "The area occupied by a solar or wind installation can be co-opted for other purposes.",
            "No mass is consumed when using solar or wind power to produce electricity.",
            "Solar and wind power are intermittent unlike fossil fuels.",
            "EROI values of wind and solar are below the economic threshold of 7."
        ],
        "correct": {"No mass is consumed when using solar or wind power to produce electricity."}
    },
    {
        "question": "Producing electricity at a power plant involves a serial conversion of various types of energy.  Which of the following energy conversions has the lowest efficiency?",
        "choices": [
            "Thermal energy to Chemical energy",
            "Chemical energy to thermal energy",
            "Mechanical energy to electrical energy",
            "Thermal energy to mechanical energy"
        ],
        "correct": {"Thermal energy to mechanical energy"}
    },
    {
        "question": "Recall our discussion of the power density of a solar photovoltaic array.  The efficiency of a solar array is the proportion of solar energy that is converted to electricity.\n\nIf an area of land receives solar energy at a rate of 200 W/m2 and the efficiency of the solar array is 15%, what is the expected power density of the solar array?",
        "choices": ["1333 W/m2", "30 W/m2", "The power density cannot be calculated with the provided information.", "3000 W/m2"],
        "correct": {"30 W/m2"}
    },
    {
        "question": "Which of the following regions exhibits the highest level of energy poverty?",
        "choices": ["Sub-Saharan Africa", "North Africa", "North America", "Latin America"],
        "correct": {"Sub-Saharan Africa"}
    },
    {
        "question": "Which of the following statements is FALSE about the different types of coal mining?",
        "choices": [
            "Underground coal mining techniques vary in the proportion of coal extracted.",
            "Strip mine reclamation involves returning surface topography to its approximate original contours.",
            "Longwall mining involves placing overburden in adjacent stream valleys.",
            "Fugitive methane emissions occur at both underground and surface coal mines"
        ],
        "correct": {"Longwall mining involves placing overburden in adjacent stream valleys."}
    },
    {
        "question": "Low concentrations of metals, such as selenium, in surface waters can lead to toxicity symptoms in aquatic organisms, especially offspring, via ________.",
        "choices": ["metal excretion rates exceeding metal intake rates", "mine remediation", "bioaccumulation", "biomagnification"],
        "correct": {"bioaccumulation"}
    },
    {
        "question": "Read the following statement very carefully and determine whether it is True or False.\n\nParticles of bottom ash, a type of coal ash, are often used in cement production because they are nearly spherical, have an almost pure silica composition, and are small in size.",
        "choices": ["True", "False"],
        "correct": {"False"}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nSulfate (SO42-) concentrations in surface water can be used as a proxy for extent of coal mining in a watershed due to the ________ that occurs at both surface and underground coal mines.",
        "choices": ["fugitive methane", "bioaccumulation", "acid mine drainage", "selenium discharge"],
        "correct": {"acid mine drainage"}
    },
    {
        "question": "Choose the option that best completes the following statement.\n\nIn coal mining regions, acid mine drainage is the result of __________.",
        "choices": [
            "Oxidation of sulfur-bearing organic matter in the coal.",
            "Acids used to extract coal",
            "Pulverized limestone used as rock dust in underground mines.",
            "Oxidation of sulfur-bearing minerals (pyrite) in coal"
        ],
        "correct": {"Oxidation of sulfur-bearing minerals (pyrite) in coal"}
    },
    {
        "question": "What happens to the overburden at surface coal mines, like open pit mines and mountaintop removal mines?",
        "choices": [
            "The overburden at both types of surface mines is typically used to back fill mining pits and return the landscape to its approximate original contours (i.e., original topography).",
            "The overburden at a mountaintop removal mine is typically used to back fill mining pits and return the landscape to its approximate original contours (i.e., original topography). The overburden at an open pit mine is placed in adjacent stream valleys, resulting in a lower relief landscape.",
            "The overburden at an open pit mine is typically used to back fill mining pits and return the landscape to its approximate original contours (i.e., original topography). The overburden at a mountain top removal mine is placed in adjacent stream valleys, resulting in a lower relief landscape.",
            "The overburden at both types of surface mines is placed in adjacent stream valleys, resulting in a lower relief landscape."
        ],
        "correct": {"The overburden at an open pit mine is typically used to back fill mining pits and return the landscape to its approximate original contours (i.e., original topography). The overburden at a mountain top removal mine is placed in adjacent stream valleys, resulting in a lower relief landscape."}
    },
    {
        "question": "Which of the following terms is defined as the connectivity between open spaces in rock?",
        "choices": ["Resistivity", "Porosity", "Permeability", "Migration pathway"],
        "correct": {"Permeability"}
    },
    {
        "question": "Casing and cementing an oil production well prevents __________ . (Select all that apply)",
        "choices": [
            "flooding of seawater into the deep, hydrocarbon-producing areas of the borehole.",
            "inward collapse of the borehole.",
            "drilling mud from coming into contact with reservoir rocks during a pressure integrity test.",
            "contamination of aquifers (i.e., bodies of groundwater) that are perforated by the well."
        ],
        "correct": {"inward collapse of the borehole.", "contamination of aquifers (i.e., bodies of groundwater) that are perforated by the well."}
    },
    {
        "question": "The temperature and pressure conditions between 6 and 9 km depth that produce hydrocarbons are termed the _______.",
        "choices": ["Kerogen Window", "Oil Window", "Graphite Window", "Natural Gas Window"],
        "correct": {"Natural Gas Window"}
    },
    {
    "question": "What is a trap/seal in the context of conventional hydrocarbon systems?",
    "choices": [
      "Rock layers with a particular geometry that prevent a large volume of hydrocarbons from concentrating in one area underground.",
      "A fracture in the Earth's crust along which two blocks of earth material (i.e., hanging-wall and footwall blocks) move relative to each other.",
      "Rock layers with a particular geometry that keep a large volume of hydrocarbons locally concentrated and prevents the hydrocarbons from seeping to the surface.",
      "A natural conduit, such as a fault, through which hydrocarbons travel from the source rock to the reservoir rock."
    ],
    "correct": {"Rock layers with a particular geometry that keep a large volume of hydrocarbons locally concentrated and prevents the hydrocarbons from seeping to the surface."}
  },
  {
    "question": "Choose the option that correctly explains why the following statement is FALSE.\n\nCombustion of sulfur-bearing organic compounds in coal is the primary source of acid mine drainage.",
    "choices": [
      "Sulfur is only present in coal in the form or inorganic minerals. There are no sulfur-bearing organic compounds in coal.",
      "Acid mine drainage is primarily caused by oxidation of sulfur-bearing, inorganic minerals that are exposed at mining sites.",
      "It is the combustion of lead-bearing, not sulfur-bearing, organic compounds that produces acid mine drainage.",
      "No acid mine drainage occurs during coal mining or combustion of coal."
    ],
    "correct": {"Acid mine drainage is primarily caused by oxidation of sulfur-bearing, inorganic minerals that are exposed at mining sites."}
  },
  {
    "question": "What percentage of U.S. energy (i.e., total energy consumption) was derived from fossil fuels in 2023?",
    "choices": [
      "60-69%",
      "80-89%",
      "50-59%",
      "70-79%"
    ],
    "correct": {"80-89%"}
  },
  {
    "question": "Which of the following energy resources has the highest energy density?",
    "choices": [
      "Natural Gas",
      "Coal",
      "Oil",
      "Wind"
    ],
    "correct": {"Natural Gas"}
  },
  {
    "question": "What is burial diagenesis?",
    "choices": [
      "The gradual sinking of crust without significant deformation.",
      "All the chemical and physical changes experienced by Earth materials as they are buried under the Earth’s surface.",
      "The process responsible for peat formation in coastal wetlands.",
      "All the chemical and physical changes experienced by sediment at the seafloor."
    ],
    "correct": {"All the chemical and physical changes experienced by Earth materials as they are buried under the Earth’s surface."}
  },
  {
    "question": "Which of the following options is NOT a unit of power?",
    "choices": [
      "British Thermal Unit per Hour (Btu/hr)",
      "Gigawatt (GW)",
      "Kilowatt (kW)",
      "Kilowatt-hour (kWh)"
    ],
    "correct": {"Kilowatt-hour (kWh)"}
  },
  {
    "question": "There is substantial economic inertia against transitioning away from a fossil fuel-dominated energy economy in the U.S.\n\nWhich of the following is NOT a contributing factor to this inertia?",
    "choices": [
      "extensive infrastructure supporting fossil fuel consumption",
      "comparably high EROI values for renewable energy resources",
      "financial contributions to political campaigns by fossil fuel companies",
      "fossil fuel revenues"
    ],
    "correct": {"comparably high EROI values for renewable energy resources"}
  },
  {
    "question": "Which of the following statements is TRUE regarding mountaintop removal mining + valley fill (MTM/VF) and selenium in stream water?",
    "choices": [
      "Once a valley fill has been deemed reclaimed by regulatory standards, the fill will stop emitting selenium to stream water within a year.",
      "The water concentration of selenium within a watershed increases as more of the watershed is disturbed by MTM/VF operations.",
      "There are no records of reclaimed MTM/VF sites emitting selenium into stream water.",
      "There is no relationship between the size or volume of a valley fill and the amount of selenium it emits to stream water."
    ],
    "correct": {"The water concentration of selenium within a watershed increases as more of the watershed is disturbed by MTM/VF operations."}
  },
  {
    "question": "There are many economic risks of not reducing fossil fuel consumption in regional and global energy systems.\n\nWhich of the following options is NOT one of these risks?",
    "choices": [
      "Gradual decline in energy returned on investment (EROI) of nuclear and renewables.",
      "Substantial decrease in economic activity and gross domestic product (GDP) due to climate change.",
      "The economic cost of environmental disasters associated with producing and transporting fossil fuels (e.g., Deepwater Horizon Disaster).",
      "Loss of investment in the context of the Carbon Bubble."
    ],
    "correct": {"Gradual decline in energy returned on investment (EROI) of nuclear and renewables."}
  },
  {
    "question": "One of the \"myths\" regarding energy poverty, as described in our Week 2 reading assignment, is ______________ .",
    "choices": [
      "that climate change should not be considered when deciding how to solve energy poverty.",
      "that providing reliable energy to the industrial sector of a developing country takes priority over the commercial sector.",
      "that developing countries will skip an industrialization stage, and the associated need for high capacity energy systems, on their way out of energy poverty.",
      "that lights and air conditioning equal a modern energy system."
    ],
    "correct": {"that developing countries will skip an industrialization stage, and the associated need for high capacity energy systems, on their way out of energy poverty."}
  },
  {
    "question": "The US Environmental Protection Agency (EPA) classifies coal ash as a non-hazardous waste and has established rules for coal ash disposal similar to those for household garbage.",
    "choices": [
      "True",
      "False"
    ],
    "correct": {"True"}
  },
  {
    "question": "The power density of ________ is inherently constrained by the power capacity of photosynthetic organisms per area, which is on average ________ W/m2.",
    "choices": [
      "coal; ~400",
      "biofuels; ~0.2",
      "solar energy; ~30",
      "wind energy; ~30"
    ],
    "correct": {"biofuels; ~0.2"}
  },
  {
    "question": "Imagine that a coal-fired power plant has the option to buy either a lignite coal with 5% sulfur content or a bituminous coal with 2% sulfur content.\n\nAssuming both types of coal have the same price, which type of coal would be preferred by the power plant operators?  Why?",
    "choices": [
      "The bituminous coal with 2% sulfur content would be preferred, because it has a higher energy density.  Less effort and expense would be required to reduce sulfur emissions from the power plant once the coal was burned.",
      "The lignite coal with 5% sulfur content would be preferred, because it has a higher energy density.  Less effort and expense would be required to reduce sulfur emissions from the power plant once the coal was burned.",
      "The bituminous coal with 2% sulfur content would be preferred, because it has a lower energy density.  Less effort and expense would be required to reduce sulfur emissions from the power plant.",
      "The lignite coal with 5% sulfur content would be preferred, because it has a lower water content.  Less effort and expense would be required to reduce sulfur emissions from the power plant."
    ],
    "correct": {"The bituminous coal with 2% sulfur content would be preferred, because it has a higher energy density.  Less effort and expense would be required to reduce sulfur emissions from the power plant once the coal was burned."}
  },
  {
    "question": "Choose the option that correctly completes the following statement.\n\n__________ can lead to acid deposition (i.e., dry acid deposition and acid rain) when coal is burned to generate electricity.",
    "choices": [
      "The incombustible mineral matter in coal",
      "Volatiles derived from the organic component of coal",
      "Sulfur contained in the \"fixed carbon\" of coal",
      "Sulfur contained in the mineral content of coal"
    ],
    "correct": {"Sulfur contained in the \"fixed carbon\" of coal"}
  },
  {
    "question": "Longwall coal mining causes sinking, or subsidence, of the ground surface above the mine.\n\nWhich of the following is a negative consequence of this subsidence?",
    "choices": [
      "Buildings built above or near the mines may develop damaged foundations.",
      "Roads above a longwall mine may become gradually deformed over time and require additional maintenance.",
      "All of the answer options are negative consequences of longwall mine subsidence.",
      "Crops grown above the mine can more easily flood due to their lower elevation."
    ],
    "correct": {"All of the answer options are negative consequences of longwall mine subsidence."}
  },
  {
    "question": "Why is it more difficult to estimate the power density of an energy resource, like coal, than it is to estimate its energy density?",
    "choices": [
      "When measuring energy density, you measure the mass of coal and the amount of heat it produces when you burn it.\n\nAn accurate power density estimate requires a full life cycle approach, in which one needs to evaluate energy returned on investment (EROI) in every stage of production and power generation.",
      "When measuring energy density, you measure the mass of coal and the amount of heat it produces when you burn it.\n\nAn accurate power density estimate requires a full life cycle approach, in which one needs to evaluate all of the land used when producing and utilizing the resource.",
      "When measuring energy density, you measure the mass of coal and the amount of heat it produces when you burn it.\n\nAn accurate power density estimate requires an historical approach, in which one needs to evaluate the energy intensity of the nation using the resource.",
      "I don't know what you are talking about.  The first homework assignment clearly demonstrated that power density estimates are easier to calculate than energy density."
    ],
    "correct": {"When measuring energy density, you measure the mass of coal and the amount of heat it produces when you burn it.\n\nAn accurate power density estimate requires a full life cycle approach, in which one needs to evaluate all of the land used when producing and utilizing the resource."}
  },
    {
    "question": "Choose the option that best completes the following statement.\n\nUnder increasing heat and pressure, the formation of conventional hydrocarbons proceeds in a prescribed order as follows ________ .",
    "choices": [
      "Organic remains, kerogen, oil, natural gas",
      "Organic remains, kerogen, graphite, oil, natural gas",
      "Peat, lignite, sub-bituminous, bituminous, anthracite",
      "Coal, bitumen, oil and natural gas"
    ],
    "correct": {"Organic remains, kerogen, oil, natural gas"}
  },
  {
    "question": "\"Cooked”, wax-like organic matter that is the precursor to oil and natural gas is called ________ .",
    "choices": [
      "Bitumen",
      "Kerogen",
      "Graphite",
      "Plankton"
    ],
    "correct": {"Kerogen"}
  },
  {
    "question": "From which country does the United States derive most of its oil imports?",
    "choices": [
      "Iraq",
      "Canada",
      "Saudi Arabia",
      "Venezuela"
    ],
    "correct": {"Canada"}
  },
  {
    "question": "Which of the following units would be best for describing the amount of electricity you consume each month?",
    "choices": [
      "Kilowatt (kW)",
      "Power density (watts per square meter)",
      "British Thermal Unit (Btu) per hour",
      "Kilowatt-hour (kWh)"
    ],
    "correct": {"Kilowatt-hour (kWh)"}
  },
  {
    "question": "Which of the following best describes the meaning of economic sustainability at a national scale?",
    "choices": [
      "A nation that provides a good quality of life (e.g., education, health, and equality) for current citizens and future generations.",
      "A nation that uses its resources efficiently and responsibly in such a manner that allows continued economic activity and long-term economic growth.",
      "A nation that produces sufficient economic prosperity to support the current generation of citizens.",
      "A nation that operates within the means of natural systems that provide resources and a sink for wastes."
    ],
    "correct": {"A nation that uses its resources efficiently and responsibly in such a manner that allows continued economic activity and long-term economic growth."}
  },
  {
    "question": "Read the following statement very carefully and determine if it is True or False.\n\nIn his TED talk entitled \"Magic Washing Machine\", statistician Hans Rosling argues that future population growth and economic stagnation in developing countries will greatly increase global energy consumption.",
    "choices": [
      "True",
      "False"
    ],
    "correct": {"False"}
  },
  {
    "question": "Which of the following statements is FALSE regarding the importance of plate tectonic processes and energy resources?",
    "choices": [
      "Tectonic stresses cause subsidence.  Subsidence causes organic material to become buried in the crust where it is transformed into fossil fuels.",
      "Tectonic processes \"store and concentrate\" the products of photosynthesis as fossil fuels.",
      "Tectonic stresses push buried organic material up to the surface where it exposed to diagenetic processes.  These diagenetic processes transform organic material into fossil fuels.",
      "Tectonic stresses allow organic material to become buried and exposed to diagenetic processes, transforming it into fossil fuels."
    ],
    "correct": {"Tectonic stresses push buried organic material up to the surface where it exposed to diagenetic processes.  These diagenetic processes transform organic material into fossil fuels."}
  },
  {
    "question": "A thorough power density estimate should include the full life cycle of an energy resource and the technologies used to extract and/or consume it.\n\nWhich of the following scenarios could potentially lead to an increase in power density?",
    "choices": [
      "Biofuels: The global demand for sugar cane ethanol increases.  Farmers in South and Central America clear tropical forests at an increasing rate for additional sugar cane production.  The amount of sugar cane produced per square meter of land remains the same.",
      "Wind power: A national-scale recycling program for turbine blades is established, reducing the amount of material buried in landfills.",
      "Biofuels:  Climate change causes long-term drought in the Midwest.  Numerous reservoirs (man-made lakes) are constructed to provide sufficient irrigation water for energy crops (i.e., corn for ethanol).",
      "Coal: The demand for coal ash as structural fill decreases nationwide, increasing the amount of coal ash buried in landfills."
    ],
    "correct": {"Wind power: A national-scale recycling program for turbine blades is established, reducing the amount of material buried in landfills."}
  },
  {
    "question": "How do oil imports from Canada potentially contribute to the economic sustainability of the U.S. energy system?\n\nIn your answer, be sure to describe:\n1) the primary type of crude oil produced domestically;\n2) the primary type of crude oil imported from Canada; and\n3) how Canadian oil ensures an 'operational profit' for the U.S. oil industry.",
    "type": "free_response",
    "answer": "The primary type of crude oil produced domestically in the U.S. is light crude oil. However, many U.S. refineries are designed to process heavy crude oil, which the U.S. does not produce in large quantities. Canada supplies heavy crude oil, which allows these refineries to continue operating efficiently. This match between supply and refinery design supports 'operational profits' and thus contributes to the economic sustainability of the U.S. energy system."
    },
    {
    "type": "free_response",
    "question": "Coal contains sulfur in two general forms:  1) inorganic sulfide minerals and 2) sulfur-bearing organic molecules. \n\nBriefly explain how environment conditions during and after formation of the original peat can affect sulfur concentrations in resulting coal.  Be sure to include the role of anaerobic bacteria and the two original sources of the sulfur.",
    "answer": "Flooding by seawater delivers sulfate to the peat swamps, and anaerobic bacteria reduce that sulfate into hydrogen sulfide waste, which can react with the peat to form sulfur-bearing minerals and secondary sulfur-bearing organics."
    },
  {
    "question": "U.S. oil imports have declined since 2006.\n\nWhich of the following statements correctly describes a reason for this decline?",
    "choices": [
      "The systematic shutdown of coker units among U.S. oil refineries has lowered demand for oil imports.",
      "The lack of investment in pipeline infrastructure since 2008 has dramatically increased the price of oil, lowering the demand.",
      "The rapid adoption of all-electric vehicles has cut overall demand for oil in half.",
      "The widespread adoption of hydraulic fracturing techniques has significantly increased domestic oil production in the U.S."
    ],
    "correct": {"The widespread adoption of hydraulic fracturing techniques has significantly increased domestic oil production in the U.S."}
  },
  {
    "question": "Choose the option that best completes the following statement.\n\nCasing and cementing an oil well prevents which of the following _______ .",
    "choices": [
      "Inward collapse of the well.",
      "All of the answer options are correct.",
      "Contamination of potable groundwater sources that were intersected by the well.",
      "Uncontrolled release of fluid pressure."
    ],
    "correct": {"All of the answer options are correct."}
  },
  {
    "question": "Pressure Integrity Tests (PIT) can be used to determine if there any imperfections in the casing and cement of a production well that may allow hydrocarbon-bearing fluids to communicate with and contaminate potable groundwater resources.\n\nExamine the PIT results of a newly completed (hypothetical) production well in the graph above.\n\nWhich of the following options describes a correct interpretation of the PIT results?",
    "choices": [
      "The casing and cement of the well are intact, because the observed leak-off pressure matches the expected leak-off pressure.",
      "The casing and cement of the well are intact.  The observed leak-off pressure is much lower than the expected leak-off pressure that would occur during a catastrophic failure.",
      "There are multiple small fractures in the cement and casing, because there are multiple leak-off pressures during the test.",
      "There is a large channel or fracture in the cement casing, because the observed leak-off pressure is lower than the predicted leak-off pressure."
    ],
    "correct": {"There is a large channel or fracture in the cement casing, because the observed leak-off pressure is lower than the predicted leak-off pressure."}
  },
  {
    "type": "free_response",
    "question": "In lecture, we discussed three scientific studies on the environmental impacts of mountaintop removal mining + valley fill (MTM/VF) with respect to acid mine drainage and selenium in mining effluent (i.e., water and contaminants emitted from the mining site).  Choose one of the studies (Lindberg et al. 2011, Ross et al. 2016, or Foster et al. 2024) and briefly summarize the following:\n\n    The question or hypothesis addressed by the scientific study;\n    The methodology of the study (a rough description will be sufficient); and\n    The overall conclusion or discovery made in the study.",
    "answer": "Lindberg et al. (2011) wanted to test how multiple MTM/VF sites (both active and reclaimed) affected water quality of a single watershed.  They found an additive effect (more sites, lower water quality) and that reclaimed sites continue to release sulfuric acid, but not necessarily selenium."
}

]

# Dictionary of quiz sets
quiz_sets = {
    "Exam 4": bioenergy_flashcards,
    "Exam 3": exam3_flashcards,
    "Exam 2": exam2_flashcards,
    "Exam 1": exam1_flashcards,
    "All Topics (Exams: 1-4)": gui_flashcards
}

class FlashcardQuiz:
    def __init__(self, root, cards):
        self.root = root
        self.cards = cards
        self.index = 0
        self.score = 0
        self.answered = 0
        self.submitted = False
        self.vars = []
        self.response_entry = None

        random.shuffle(self.cards)

        self.question_label = tk.Label(root, text="", wraplength=600, font=('Arial', 14), justify="left")
        self.question_label.pack(pady=20)

        self.choice_frame = tk.Frame(root)
        self.choice_frame.pack()

        self.feedback_label = tk.Label(root, text="", font=('Arial', 12))
        self.feedback_label.pack()

        self.score_label = tk.Label(root, text="Score: 0 / 0", font=('Arial', 12))
        self.score_label.place(x=10, y=470)

        self.action_btn = tk.Button(root, text="Submit", command=self.handle_action)
        self.action_btn.pack(pady=10)

        self.display_question()

    def display_question(self):
        self.vars = []
        for widget in self.choice_frame.winfo_children():
            widget.destroy()

        card = self.cards[self.index]
        self.question_label.config(text=card["question"])
        self.submitted = False
        self.action_btn.config(text="Submit")
        self.feedback_label.config(text="")

        if card.get("type") == "free_response":
            self.response_entry = tk.Text(self.choice_frame, height=5, width=70, wrap="word")
            self.response_entry.pack()
        else:
            self.response_entry = None
            for choice in card["choices"]:
                var = tk.IntVar()
                chk = tk.Checkbutton(self.choice_frame, text=choice, variable=var, anchor='w', justify='left', wraplength=600)
                chk.pack(anchor='w')
                self.vars.append((var, choice))

    def handle_action(self):
        if not self.submitted:
            self.check_answer()
        else:
            self.next_question()

    def check_answer(self):
        card = self.cards[self.index]
        self.answered += 1

        if card.get("type") == "free_response":
            user_answer = self.response_entry.get("1.0", tk.END).strip()
            correct_answer = card["answer"]
            self.feedback_label.config(text=f"✅ Answer:\n{correct_answer}",fg="blue",wraplength=600,justify="left" )
            self.score += 1
        else:
            selected = {text for var, text in self.vars if var.get() == 1}
            correct = card["correct"]
            if selected == correct:
                self.feedback_label.config(text="✅ Correct!", fg="green")
                self.score += 1
            else:
                self.feedback_label.config(text=f"❌ Incorrect.\nCorrect answer(s): {', '.join(correct)}",fg="red",wraplength=600,justify="left")

        self.score_label.config(text=f"Score: {self.score} / {self.answered}")
        self.submitted = True
        self.action_btn.config(text="Next")


    def next_question(self):
        self.index += 1
        if self.index >= len(self.cards):
            amt = (self.score / len(self.cards)) * 100
            messagebox.showinfo("Quiz Complete", f"You scored {self.score} out of {len(self.cards)}. That's {amt:.1f}%")
            self.root.quit()
        else:
            self.display_question()

def show_welcome_screen():
    def start_quiz():
        selected_set = set_var.get()
        if selected_set in quiz_sets:
            welcome_frame.destroy()
            FlashcardQuiz(root, quiz_sets[selected_set])

    welcome_frame = tk.Frame(root)
    welcome_frame.pack(pady=100)

    tk.Label(welcome_frame, text="Welcome to the Flashcard Quiz!", font=('Arial', 16)).pack(pady=10)
    tk.Label(welcome_frame, text="Select a flashcard set to begin:", font=('Arial', 12)).pack(pady=5)

    set_var = tk.StringVar(root)
    set_var.set("Energy Mix")

    options_menu = tk.OptionMenu(welcome_frame, set_var, *quiz_sets.keys())
    options_menu.pack(pady=10)

    tk.Button(welcome_frame, text="Start Quiz", command=start_quiz).pack(pady=10)

# Launch app
root = tk.Tk()
root.title("Energy Systems Flashcard Quiz")
root.geometry("700x500")
show_welcome_screen()
root.mainloop()
