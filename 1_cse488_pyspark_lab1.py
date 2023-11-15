"""
# **Lab Assignment**

## **Problem-1**

Find the Air craft, country flying mission and target country for those missions in which time on target was less than 1000.
"""

query=  """
        SELECT AirCraft,ContryFlyingMission,TargetCountry
        FROM Bombing_operations
        WHERE TimeOnTarget<1000
        """
result=spark.sql(query)
result.show()

"""## **Problem-2**

Find the target country and the number of times they have been attacked. Show the result in descending order.
"""

query=  """
        SELECT TargetCountry, count(*) AS num_of_times
        FROM Bombing_operations
        group by TargetCountry
        order by num_of_times desc;
        """
result=spark.sql(query)
result.show()

"""## **Problem-3**

Find the target country which had been attacked most.
"""

query=  """
        select TargetCountry
        From(SELECT  TargetCountry, count(*) AS num_of_times
        FROM Bombing_operations
        group by TargetCountry
        order by num_of_times desc) LIMIT 1;
        """
result=spark.sql(query)
result.show()

"""## **Problem-4**

Find the country flying mission which attacked most.
"""

query=  """
        select ContryFlyingMission
        From(SELECT  ContryFlyingMission, count(*) AS num_of_times
        FROM Bombing_operations
        group by ContryFlyingMission
        order by num_of_times desc) LIMIT 1;
        """
result=spark.sql(query)
result.show()

"""## **Problem-5**

Find the take off location and how many times they had used.
"""

query = """
        SELECT TakeoffLocation, count(*) AS numOfTimes
        FROM Bombing_operations
        group by TakeoffLocation
        order by numOfTimes desc
        """
result = spark.sql(query)
result.show()

"""## **Problem-6**

Find the number of fighter jets from Aircraft_Glossary.
"""

Aircraft_glossary.createOrReplaceTempView("Aircraft_Glossary")

query = """
        SELECT  count(AirCraftType) as Fighter_Jet
        FROM Aircraft_Glossary
        where AirCraftType=='Fighter Jet' or AirCraftType=='Fighter jet ' ;
        """
result = spark.sql(query)
result.show()

"""## **Problem-7**

Find the number of different types air craft for each air craft type.
"""

query=  """
        SELECT AirCraftType, count(*) AS num_of_times
        FROM Aircraft_glossary
        group by AirCraftType
        """
result=spark.sql(query)
result.show()

"""## **Problem-8**

Find the air craft name which had used most in attacks.
"""

query=  """
        SELECT AirCraft
           from(SELECT b.AirCraft , count(*) as most_use
        FROM Aircraft_glossary a,Bombing_operations b
        where a.AirCraft=b.AirCraft
        group by b.AirCraft
        order by most_use desc) LIMIT 1

        """
result=spark.sql(query)
result.show()
