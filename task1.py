
class Interval:
   def __init__(self, start, end):
      if (isinstance(start,(int,float)) and isinstance(end,(int, float))) is False:
         raise ValueError("Both start and end must be numeric (either integers or floats)")
      if start > end:
         raise ValueError("start must be less than or equal to end")
      self.start = start
      self.end = end

   def __str__(self):
      return f"[{self.start},{self.end}]"
   
   def is_overlapping(self, other_interval):
      if self.end >= other_interval.start and self.start<= other_interval.end:
         return True
      else:
         return False
      
   @staticmethod
   def intersection_static(interval1, interval2):
      if interval1.is_overlapping(interval2):
         start = max(interval1.start, interval2.start)
         end = min(interval1.end, interval2.end)
         return Interval (start, end)
      else:
         return None
      
   def __and__(self, other):
      if not isinstance(other,(int, Interval)):
         raise  ValueError("other must be int or Interval")
      return Interval.intersection_static(self, other)

   @staticmethod
   def union_static(interval1, interval2):
      if interval1.is_overlapping(interval2):
         start = min(interval1.start, interval2.start)
         end = max(interval1.end, interval2.end)
         return Interval (start, end)
      else:
         return None
      
   def __or__(self, other_interval):
      if not isinstance(other_interval,(int, Interval)):
         raise  ValueError("other must be int or Interval")
      return Interval.union_static(self, other_interval)
   

   
interval_1 = Interval(1, 5)
print(interval_1)

interval_2 = Interval(3, 8)

overlap_result = interval_1.is_overlapping(interval_2) 
print("Do intervals overlap?", overlap_result)

intersection_result_static = Interval.intersection_static(interval_1, interval_2)
print("Intersection result (static method):", intersection_result_static)

intersection_result = interval_1 & interval_2
print("Intersection_result:", intersection_result)

union_result_static = Interval.union_static(interval_1, interval_2)
print("Union Result (Static method):", union_result_static)

union_result = interval_1 | interval_2
print("Union Result:", union_result)

