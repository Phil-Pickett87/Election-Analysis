# Election Audit Analysis
Overview:
The purpose of this audit is to provide the election comission with the results of the congressional election. This analysis gives a detailed report of the number of votes cast, the counties they were cast in, and the amount of votes cast for each candidate.

Election Audit Results:
 
 * Number of Votes Cast: 
    * 369,711
    
 * Votes by County:
    * Arapahoe: 24,801 (6.7%)
    * Denver: 306,055 (82.8%)
    * Jefferson: 38,855 (10.5%)
  
 * County with the Most Votes: 
    * Denver
    
 * Votes Cast for Each Candidate:
    * Charles Casper Stockham: 85,213 (23.0%)
    * Diana DeGette: 272,892 (73.8%)
    * Raymon Anthony Doane: 11,606 (3.1%)
 
 * Winner Summary:
    * Winning Candidate: Dianna DeGette
    * Winning Vote Count: 272,892
    * Percentage of total votes recieved: 73.8%
    
Election Audit Summary: 
With this script, extracting the important information from the data set is easy, clear, and concise. With the way the script has been formatted it is relatively easy to apply it to other election data sets to acheive the same output. At the beginning of the script if we choose a different "file_to_load" (for example a data set from a different campaign) we will be able to run the code and get the same data output as we have gotten with this campaign. However, say the data set we recieved was a national election and instead of breaking down the data by county, we wanted to break it down state by state. With it a bit of restructuring we could change where our script commands read "county" to "state". So instead of "county_name" it would be "state_name", instead of "largest_county_turnout" it would read "largest_state_turnout" and so on. It is easy to see how with simple modifications this script can be manipulated and applied to any election data to achieve the desired output!
