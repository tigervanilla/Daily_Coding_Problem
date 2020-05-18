'''
This problem was asked by Facebook.

Given an unordered list of flights taken by someone,
each represented as (origin, destination) pairs,
and a starting airport,
compute the person's itinerary. If no such itinerary exists, return null.
If there are multiple possible itineraries, return the lexicographically smallest one.
All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
and starting airport 'YUL'
you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')]
and starting airport 'COM'
you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
and starting airport 'A'
you should return the list ['A', 'B', 'C', 'A', 'C']
even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
However, the first one is lexicographically smaller.
'''

def getItinerary(flights, currentItinerary):
  if not flights:
    return currentItinerary

  lastAirport = currentItinerary[-1]
  for i, (src, dest) in enumerate(flights):
    if lastAirport == src:
      flightsMinusCurrent = flights[:i] + flights[i+1:]
      currentItinerary.append(dest)
      return getItinerary(flightsMinusCurrent, currentItinerary)
  return None


# Driver code:
testcases = [
  {
    'flights': [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')],
    'source': ['YUL']
  },
  {
    'flights': [('SFO', 'COM'), ('COM', 'YYZ')],
    'source': ['COM']
  },
  {
    'flights': [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] ,
    'source': ['A']
  }
]
for tc in testcases:
    print(getItinerary(tc['flights'], tc['source']))
