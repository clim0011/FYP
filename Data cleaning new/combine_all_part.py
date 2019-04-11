Netherlands_df = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
Kingdom_df = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
France_df = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
Spain_df = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
Italy_df = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
Austria_df = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])

Netherlands_df.append(Netherlands_df_1, ignore_index = True)
Kingdom_df.append(Kingdom_df_1, ignore_index = True)
France_df.append(France_df_1, ignore_index = True)
Spain_df.append(Spain_df_1, ignore_index = True)
Italy_df.append(Italy_df_1, ignore_index = True)
Austria_df.append(Austria_df_1, ignore_index = True)

Netherlands_df.append(Netherlands_df_2, ignore_index = True)
Kingdom_df.append(Kingdom_df_2, ignore_index = True)
France_df.append(France_df_2, ignore_index = True)
Spain_df.append(Spain_df_2, ignore_index = True)
Italy_df.append(Italy_df_2, ignore_index = True)
Austria_df.append(Austria_df_2, ignore_index = True)

Netherlands_df.append(Netherlands_df_3, ignore_index = True)
Kingdom_df.append(Kingdom_df_3, ignore_index = True)
France_df.append(France_df_3, ignore_index = True)
Spain_df.append(Spain_df_3, ignore_index = True)
Italy_df.append(Italy_df_3, ignore_index = True)
Austria_df.append(Austria_df_3, ignore_index = True)

Netherlands_df.append(Netherlands_df_4, ignore_index = True)
Kingdom_df.append(Kingdom_df_4, ignore_index = True)
France_df.append(France_df_4, ignore_index = True)
Spain_df.append(Spain_df_4, ignore_index = True)
Italy_df.append(Italy_df_4, ignore_index = True)
Austria_df.append(Austria_df_4, ignore_index = True)

Netherlands_df.append(Netherlands_df_5, ignore_index = True)
Kingdom_df.append(Kingdom_df_5, ignore_index = True)
France_df.append(France_df_5, ignore_index = True)
Spain_df.append(Spain_df_5, ignore_index = True)
Italy_df.append(Italy_df_5, ignore_index = True)
Austria_df.append(Austria_df_5, ignore_index = True)

Netherlands_df.to_csv('Netherlands_review.csv',index = False)
Kingdom_df.to_csv('Kingdom_review.csv',index = False)
France_df.to_csv('France_review.csv',index = False)
Spain_df.to_csv('Spain_review.csv',index = False)
Italy_df.to_csv('Italy_review.csv',index = False)
Austria_df.to_csv('Austria_review.csv',index = False)
