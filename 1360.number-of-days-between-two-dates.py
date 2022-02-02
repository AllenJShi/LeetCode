#
# @lc app=leetcode id=1360 lang=python
#
# [1360] Number of Days Between Two Dates
#

# @lc code=start
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        # date1 = datetime.datetime.strptime(date1,'%Y-%m-%d')
        # date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
        # return abs((date1-date2).days)
        
        
        
        
        ###### 参考答案 #########
        def leap_year(year):
            # 闰年是4的倍数但不是100的倍数，是400的倍数
            return year%400==0 or (year%100!=0 and year%4==0)
        def date_to_int(year, month, day):
            month_length = [0,31,28,31,30,31,30,31,31,30,31,30,31]
            ans = day-1
            while month != 0:
                month -= 1
                ans += month_length[month]
                if month == 2 and leap_year(year):
                    ans += 1
            ans += 365 * (year - 1971)
            ans += (year - 1) // 4 - 1971 // 4
            ans -= (year - 1) // 100 - 1971 // 100
            ans += (year - 1) // 400 - 1971 // 400
            return ans
        date1 = [int(i) for i in date1.split('-')]
        date2 = [int(i) for i in date2.split('-')]
        return abs(date_to_int(*date1) - date_to_int(*date2))
    
# @lc code=end

