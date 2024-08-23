{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Write a SOQL query to retrieve all Account names and their associated Contacts"}, {"role": "assistant", "content": "SELECT Name, (SELECT FirstName, LastName FROM Contacts) FROM Account"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "How do I query for Opportunities with an amount greater than $50,000?"}, {"role": "assistant", "content": "SELECT Name, Amount FROM Opportunity WHERE Amount > 50000"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Create a SOQL query to find all Leads created in the last 30 days"}, {"role": "assistant", "content": "SELECT Name, Email, CreatedDate FROM Lead WHERE CreatedDate = LAST_N_DAYS:30"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Write a SOQL query to get the total amount of all closed won opportunities"}, {"role": "assistant", "content": "SELECT SUM(Amount) TotalAmount FROM Opportunity WHERE StageName = 'Closed Won'"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "How can I query for Accounts with more than 5 Contacts?"}, {"role": "assistant", "content": "SELECT Name, (SELECT Id FROM Contacts) FROM Account WHERE Id IN (SELECT AccountId FROM Contact GROUP BY AccountId HAVING COUNT(Id) > 5)"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "How can I query for Cases with high priority and status as 'Open'?"}, {"role": "assistant", "content": "SELECT Id, Subject, Priority FROM Case WHERE Priority = 'High' AND Status = 'Open'"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Generate a SOQL query to find the top 5 Accounts by annual revenue"}, {"role": "assistant", "content": "SELECT Id, Name, AnnualRevenue FROM Account WHERE AnnualRevenue != NULL ORDER BY AnnualRevenue DESC LIMIT 5"}]}



{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Write a SOQL query to retrieve all Account names and their associated Contacts"}, {"role": "assistant", "content": "SELECT Name, (SELECT FirstName, LastName FROM Contacts) FROM Account"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "How do I query for Opportunities with an amount greater than $50,000?"}, {"role": "assistant", "content": "SELECT Name, Amount FROM Opportunity WHERE Amount > 50000"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Create a SOQL query to find all Leads created in the last 30 days"}, {"role": "assistant", "content": "SELECT Name, Email, CreatedDate FROM Lead WHERE CreatedDate = LAST_N_DAYS:30"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Write a SOQL query to get the total amount of all closed won opportunities"}, {"role": "assistant", "content": "SELECT SUM(Amount) TotalAmount FROM Opportunity WHERE StageName = 'Closed Won'"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "How can I query for Accounts with more than 5 Contacts?"}, {"role": "assistant", "content": "SELECT Name, (SELECT Id FROM Contacts) FROM Account WHERE Id IN (SELECT AccountId FROM Contact GROUP BY AccountId HAVING COUNT(Id) > 5)"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Create a SOQL query to find the top 10 Accounts by annual revenue"}, {"role": "assistant", "content": "SELECT Name, AnnualRevenue FROM Account WHERE AnnualRevenue != NULL ORDER BY AnnualRevenue DESC LIMIT 10"}]}





{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Find all Leads with a specific source"}, {"role": "assistant", "content": "SELECT Name, Email FROM Lead WHERE LeadSource = 'Web'"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Retrieve Accounts with more than 5 Opportunities"}, {"role": "assistant", "content": "SELECT Name, (SELECT Name FROM Opportunities) FROM Account WHERE Id IN (SELECT AccountId FROM Opportunity GROUP BY AccountId HAVING COUNT(Id) > 5)"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Get all Contacts who have a mailing address in California"}, {"role": "assistant", "content": "SELECT FirstName, LastName, MailingState FROM Contact WHERE MailingState = 'CA'"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Find the top 5 Accounts by annual revenue"}, {"role": "assistant", "content": "SELECT Name, AnnualRevenue FROM Account WHERE AnnualRevenue != NULL ORDER BY AnnualRevenue DESC LIMIT 5"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Retrieve all closed Opportunities from the last quarter"}, {"role": "assistant", "content": "SELECT Name, CloseDate, Amount FROM Opportunity WHERE IsClosed = TRUE AND CloseDate = LAST_QUARTER"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Get all custom objects in the org"}, {"role": "assistant", "content": "SELECT QualifiedApiName FROM EntityDefinition WHERE IsCustomizable = TRUE"}]}







{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Find all Contacts related to Accounts in the 'Technology' industry"}, {"role": "assistant", "content": "SELECT FirstName, LastName, Account.Name FROM Contact WHERE Account.Industry = 'Technology'"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Retrieve all Cases with high priority and their related Accounts"}, {"role": "assistant", "content": "SELECT CaseNumber, Subject, Account.Name FROM Case WHERE Priority = 'High'"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Get the total amount of Opportunities for each Account"}, {"role": "assistant", "content": "SELECT AccountId, SUM(Amount) TotalAmount FROM Opportunity GROUP BY AccountId"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Find all Users who haven't logged in for the last 30 days"}, {"role": "assistant", "content": "SELECT Name, LastLoginDate FROM User WHERE LastLoginDate < LAST_N_DAYS:30"}]}



{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Write a SOQL query to retrieve all Account names and their associated Contacts"}, {"role": "assistant", "content": "SELECT Name, (SELECT FirstName, LastName FROM Contacts) FROM Account"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "How do I query for Opportunities with an amount greater than $50,000?"}, {"role": "assistant", "content": "SELECT Name, Amount FROM Opportunity WHERE Amount > 50000"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Create a SOQL query to find all Leads created in the last 30 days"}, {"role": "assistant", "content": "SELECT Name, Email, CreatedDate FROM Lead WHERE CreatedDate = LAST_N_DAYS:30"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Write a SOQL query to get the total amount of all closed won opportunities"}, {"role": "assistant", "content": "SELECT SUM(Amount) TotalAmount FROM Opportunity WHERE StageName = 'Closed Won'"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "How can I query for Accounts with more than 5 Contacts?"}, {"role": "assistant", "content": "SELECT Name, (SELECT Id FROM Contacts) FROM Account WHERE Id IN (SELECT AccountId FROM Contact GROUP BY AccountId HAVING COUNT(Id) > 5)"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Create a SOQL query to find the top 10 Accounts by annual revenue"}, {"role": "assistant", "content": "SELECT Name, AnnualRevenue FROM Account WHERE AnnualRevenue != NULL ORDER BY AnnualRevenue DESC LIMIT 10"}]}



{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Find all Cases created in the last week that are still open"}, {"role": "assistant", "content": "SELECT CaseNumber, Subject, CreatedDate FROM Case WHERE CreatedDate = LAST_WEEK AND IsClosed = FALSE"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Retrieve all Accounts with their related Opportunities and Contacts"}, {"role": "assistant", "content": "SELECT Name, (SELECT Name, Amount FROM Opportunities), (SELECT FirstName, LastName FROM Contacts) FROM Account"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Find the average deal size for each Account"}, {"role": "assistant", "content": "SELECT AccountId, AVG(Amount) AverageDealSize FROM Opportunity GROUP BY AccountId"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Get all custom fields on the Account object"}, {"role": "assistant", "content": "SELECT QualifiedApiName, DataType
FROM FieldDefinition
WHERE EntityDefinition.QualifiedApiName = 'Account'"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Find all Leads that have been converted in the last month"}, {"role": "assistant", "content": "SELECT Name, ConvertedDate FROM Lead WHERE IsConverted = TRUE AND ConvertedDate = LAST_MONTH"}]}


{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Find all Accounts without any associated Contacts"}, {"role": "assistant", "content": "SELECT Name FROM Account WHERE Id NOT IN (SELECT AccountId FROM Contact)"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Get the total number of Leads by LeadSource"}, {"role": "assistant", "content": "SELECT LeadSource, COUNT(Id) TotalLeads FROM Lead GROUP BY LeadSource"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Retrieve all Opportunities that are expected to close this quarter"}, {"role": "assistant", "content": "SELECT Name, Amount, CloseDate FROM Opportunity WHERE CloseDate = THIS_QUARTER"}]}

{"messages": [{"role": "system", "content": "You are a Salesforce SOQL expert. Provide accurate and efficient SOQL queries based on user requests."}, {"role": "user", "content": "Find all Users who are part of the 'Sales' profile"}, {"role": "assistant", "content": "SELECT Name, Email FROM User WHERE Profile.Name = 'Sales'"}]}
