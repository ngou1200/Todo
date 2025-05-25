from datetime import datetime, timedelta
import pytz

class DateUtils:
    @staticmethod
    def get_current_datetime():
        return datetime.now(pytz.UTC)
    
    @staticmethod
    def format_datetime(dt, format="%Y-%m-%d %H:%M:%S"):
        if dt:
            return dt.strftime(format)
        return ""
    
    @staticmethod
    def parse_datetime(dt_str, format="%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(dt_str, format)
        except (ValueError, TypeError):
            return None
    
    @staticmethod
    def get_date_range(range_type):
        now = datetime.now(pytz.UTC)
        
        if range_type == "today":
            start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            end = start + timedelta(days=1)
        elif range_type == "week":
            start = now - timedelta(days=now.weekday())
            start = start.replace(hour=0, minute=0, second=0, microsecond=0)
            end = start + timedelta(days=7)
        elif range_type == "month":
            start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            if now.month == 12:
                end = now.replace(year=now.year + 1, month=1, day=1)
            else:
                end = now.replace(month=now.month + 1, day=1)
        else:
            return None, None
            
        return start, end
    
    @staticmethod
    def is_overdue(due_date):
        if not due_date:
            return False
        return due_date < datetime.now(pytz.UTC)
    
    @staticmethod
    def get_relative_time(dt):
        if not dt:
            return ""
            
        now = datetime.now(pytz.UTC)
        diff = now - dt
        
        if diff.days < 0:
            if diff.days > -7:
                return f"In {abs(diff.days)} days"
            elif diff.days > -30:
                weeks = abs(diff.days) // 7
                return f"In {weeks} weeks"
            elif diff.days > -365:
                months = abs(diff.days) // 30
                return f"In {months} months"
            else:
                years = abs(diff.days) // 365
                return f"In {years} years"
        elif diff.days == 0:
            if diff.seconds < 3600:
                minutes = diff.seconds // 60
                return f"{minutes} minutes ago"
            else:
                hours = diff.seconds // 3600
                return f"{hours} hours ago"
        else:
            if diff.days < 7:
                return f"{diff.days} days ago"
            elif diff.days < 30:
                weeks = diff.days // 7
                return f"{weeks} weeks ago"
            elif diff.days < 365:
                months = diff.days // 30
                return f"{months} months ago"
            else:
                years = diff.days // 365
                return f"{years} years ago"