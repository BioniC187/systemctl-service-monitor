class Service:
  serviceName = ''
  displayName = ''

  def __init__(self, rawText: str):
    splitData = rawText.split('=')
    self.serviceName = splitData[0]
    if len(splitData) == 2:      
      self.displayName = splitData[1]
    else:
      self.displayName = splitData[0]