from mrakun import RakunDetector
from nltk.corpus import stopwords
import nltk
import glob
import os

#nltk.download('stopwords')
#nltk.download('punkt')
##taking document as input
text_file = open(r'C:\Users\prasad\Desktop\SKT_writ\SKT_writ_summ.txt' , encoding="utf8", errors='ignore')
text = text_file.read()
text_file.close()
#blob_text = "Brexit (/ˈbrɛksɪt, ˈbrɛɡzɪt/;[1] a portmanteau of \"British\" and \"exit\") is the scheduled withdrawal of the United Kingdom (UK) from the European Union (EU). Following a June 2016 referendum, in which 51.9% voted to leave, the UK government formally announced the country's withdrawal in March 2017, starting a two-year process that was due to conclude with the UK withdrawing on 29 March 2019. As the UK parliament thrice voted against the negotiated withdrawal agreement, that deadline has been extended twice, and is currently 31 October 2019.[2][3] An Act of Parliament requires the government to seek a third extension if no agreement is reached before 19 October. Withdrawal is advocated by Eurosceptics and opposed by pro-Europeanists, both of whom span the political spectrum. The UK joined the European Communities (EC) in 1973, with continued membership endorsed in a 1975 referendum. In the 1970s and 1980s, withdrawal from the EC was advocated mainly by the political left, e.g. in the Labour Party's 1983 election manifesto. From the 1990s, the eurosceptic wing of the Conservative Party grew, and led a rebellion over ratification of the 1992 Maastricht Treaty that established the EU. In parallel with the UK Independence Party (UKIP), and the cross-party People's Pledge campaign, it pressured Conservative Prime Minister David Cameron to hold a referendum on continued EU membership. Cameron, who had campaigned to remain, resigned after the result and was succeeded by Theresa May. On 29 March 2017, the UK government invoked Article 50 of the Treaty on European Union, formally starting the withdrawal. May called a snap general election in June 2017, which resulted in a Conservative minority government supported by the Democratic Unionist Party. UK–EU withdrawal negotiations began later that month. The UK negotiated to leave the EU customs union and single market. This resulted in the November 2018 withdrawal agreement, but the UK parliament voted against ratifying it three times. The Labour Party wanted any agreement to maintain a customs union, while many Conservatives opposed the agreement's financial settlement on the UK's share of EU financial obligations, as well as the Irish backstop designed to prevent border controls in Ireland. The Liberal Democrats, Scottish National Party and others seek to reverse Brexit through a second referendum. The EU has declined a re-negotiation that omits the backstop. In March 2019, the UK parliament voted for May to ask the EU to delay Brexit until October. Having failed to pass her agreement, May resigned as Prime Minister in July and was succeeded by Boris Johnson. He sought to replace parts of the agreement and vowed to leave the EU by the new deadline, with or without an agreement."
#text = "THE HIGH COURT FOR THE STATE OF TELANGANA AT HYDERABAD W.P.NO. B. Sankara Rao S/o Late B. Malla Rao, Aged about 39 years, Occ : Chartered Accountant, R/o Flat no 12, SK Towers, Begumpet, Hyderabad-500016. The State of Telangana,Rep., by its Principal Secretary,Municipal Administration and UrbanDevelopment Department, Secretariat,Hyderabad. The Deputy City Planner,GHMC, Hyderabad (HO). Kontham Narsing Rao S/o Late K. Swamy,Aged about 72 years, Occ : Business,R/o, West Maredpally,Secunderabad. 62, Road No.4 Threemoorthy Colony,Mahendra Hills, East Marredpally, Secunderabad. I am also deposing on behalf of Petitioners No. It is submitted that the Petitioners herein are the owners and possessors of severalapartments in “SK TOWERS” bearing municipal No. It is submitted that thepetitioners became the owners and possessors of apartments in the above named“SK TOWERS” through various sale deeds executed by Mr. K. Narsingh Rao and14 others belonging to the Kontham family represented by their G.P.A Holderwho is Respondent No.9 herein. 56632/07/08/2014/HO dated 13.10.2014 from RespondentNo.2 with zero deviations and the apartments were occupied by owners andpossessors from 2014 onwards. 209 situated at Brahmanwadi, Begumpet village. It is submitted that the being aware of the above scenario,Respondents No. It is submitted that as per the Development Agreement cum Irrevocable General Power of Attorney dated 10.07.2006 entered into by Respondents 10 to 14 and 10 others and Respondent No.9, no rights were reserved to Respondents No. 10 to 14 and 10 others to use any approach road through “SK TOWERS” to approach their land situated to the north of “SK TOWERS”. 10 to 14 have intentionally misrepresented the same10. It is submitted that the welfare association of which the petitioners are a part of replied immediately stating that the same must be discussed by the committee and in the mean time no JCB or men can be sent for any work on their land. 17 along with several henchmen brought one JCB to start the ground clearance work despite no permission from the association of “SK TOWERS”. It is submitted that they had arrived again on the next day, however permission was denied once again. 7 and 8 on 23.02.2020 and obtained an acknowledgement for the same. Several attempts were made on the same day by them to threaten and scare the petitioners and other residents. The same was witnessed by several police personnel who were present. However to their surprise, Respondents No. 8 did not register our complaint and in turn asked us to settle the matter. 10 to 17 are harassing the residents of the building by using the approach road situated within “SK TOWERS”, for the entry of heavy machinery and vehicles along with several laborers disrupting the peaceof the residents and making the entrance to apartment very dangerous and unsafe to children and senior citizens causing inconvenience and nuisance to the residents of “SK TOWERS”. In view of the above, the Petitioner herein is left with no other option other than approaching this Hon’ble Court seeking indulgence of this Hon’ble court to direct Respondents No. 2 to 6 not to award building permission to Respondents No. For the reasons sated above and those reasons those may be adduced at the time of hearing, it is prayed that this Hon’ble court may be pleased to grant an order or direction or writ, more so in the nature of writ of mandamus declaring the inaction of the Respondent No. 2 to 6 in considering the representation dated 10.03.2020 made by the Petitioners herein against Respondents No."
##defining parameters
hyperparameters = {"distance_threshold":2,
                   "distance_method": "editdistance",
                   "num_keywords" : 10,
                   "pair_diff_length":2,
                   "stopwords" : stopwords.words('english'),
                   "bigram_count_threshold":2,
                   "num_tokens":[1,2],
		   "max_similar" : 3, ## n most similar can show up n times
		   "max_occurrence" : 3} ## maximum frequency overall

##function to detect keywords in the document       
def word_detector(blob_text):
  keyword_detector = RakunDetector(hyperparameters)
  keywords= keyword_detector.find_keywords(blob_text, input_type = "text")
  #print(type(keywords))
  keyword_detector.verbose = False
  words = [i for i,j in keywords]
  #print("Keywords identified are: ", words)
  #keyword_detector.visualize_network()

  return(words)


#calling function
os.chdir(r'C:\Users\prasad\Desktop\SKT_writ\textfiles')
myfiles= glob.glob('*.txt')

for file in myfiles:
  myfile = open(file, encoding="utf8", errors='ignore')
  text = myfile.read()
  myfile.close()
  keywords = word_detector(text)

  print("Keywords identified are: ", keywords)
  #writing the list of keywords into the textfile
  with open(file, "a") as outfile:
    outfile.write("\n")
    outfile.write(",".join(keywords))
    
