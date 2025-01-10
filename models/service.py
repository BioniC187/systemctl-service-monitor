class Service:
  serviceName = ''
  displayText = ''

  def __init__(self, rawText: str):
    splitData = rawText.split('=')
    self.serviceName = splitData[0]
    if len(splitData) == 2:      
      self.displayText = splitData[1]
    else:
      self.displayText = splitData[0]