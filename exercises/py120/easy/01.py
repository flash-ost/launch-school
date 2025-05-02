"""
Banner Class
Behold this incomplete class for constructing boxed banners:

class Banner:
    def __init__(self, message):
        pass

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        pass

    def _horizontal_rule(self):
        pass

    def _message_line(self):
        return f"| {self.message} |"
Complete this class so that the test cases shown below work as intended. You are free to add any methods or instance variables you need. However, methods prefixed with an underscore are intended for internal use and should not be called externally.

You may assume that the input will always fit in your terminal window.

Test Cases
# Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+

# Further Exploration
Modify this class so that the __init__ method optionally lets you specify a fixed banner width when the Banner object is created. The message in the banner should be centered within the banner of that width. Decide for yourself how you want to handle widths that are either too narrow or too wide.
"""

class Banner:
    MAX_WIDTH = 115
    def __init__(self, message, width=None):

        if len(message) > Banner.MAX_WIDTH - 2:
            raise ValueError('Message too large')
        self.message = message

        if width:
            if not isinstance(width, int):
                raise TypeError('Width should be an integer')
            elif width < len(message) + 2:
                raise ValueError('Banner too narrow')
            elif width > Banner.MAX_WIDTH:
                raise ValueError('Banner too wide')
        self.width = width    

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        if self.width:
            return f'|{' ' * self.width}|'
        else:
            return f'|{' ' * (len(self.message) + 2)}|'

    def _horizontal_rule(self):
        if self.width:
            return f'+{'-' * self.width}+'
        else:
            return f'+{'-' * (len(self.message) + 2)}+'

    def _message_line(self):
        if self.width:
            blank = self.width - len(self.message)
            left_offset = blank // 2
            right_offset = blank - left_offset
            return f'|{' ' * left_offset}{self.message}{' ' * right_offset}|'
        else:    
            return f'| {self.message} |'
    
banner = Banner('To boldly go where no one has gone before.', 72)
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+    