
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship


class File(Base):
  __tablename__ = "files" 
  id = Column(Integer, nullable=False)
  filename = Column(String(255), nullable=False)
  resource_id = Column(String(255), nullable=False)
  owner_id = Column(Integer, ForeignKey("users.id"))
  size = Column(Integer, nullable=False)
  created_at = Column(DateTime, nullable=False)
    
  def __init__(self, filename, size, created_at) -> None:
    self.filename = filename
    self.size = size
    self.created_at = created_at
    
    

class Notification(Base):
  __tablename__ = "notifications" 
  id = Column(Integer, nullable=False)
  description = Column(String(255), nullable=False)
  title = Column(String(255), nullable=False)
  short_description = Column(String(255), nullable=False)
  created_at = Column(DateTime, nullable=False)
    
  def __init__(self, description, title, short_description, created_at) -> None:
    self.description = description
    self.title = title
    self.short_description = short_description
    self.created_at = created_at
    
    

class Role(Base):
  __tablename__ = "roles" 
  id = Column(Integer, nullable=False)
  name = Column(String(255), nullable=False)
  users = relationship("User", backref="role")
    
  def __init__(self, name) -> None:
    self.name = name
    
    

class User(Base):
  __tablename__ = "users" 
  id = Column(Integer, nullable=False)
  username = Column(String(255), nullable=False)
  email = Column(String(255), nullable=False)
  role_id = Column(Integer, ForeignKey("roles.id"))
  laboratory_id = Column(Integer, ForeignKey("laboratories.id"))
  tutorial_completed = Column(Integer, nullable=False)
  notifications_read = Column(Integer, nullable=False)
  files = relationship("File", backref="user")
  dashboards = relationship("Dashboard", backref="user")
    
  def __init__(self, username, email, tutorial_completed, notifications_read) -> None:
    self.username = username
    self.email = email
    self.tutorial_completed = tutorial_completed
    self.notifications_read = notifications_read
    
    

class Lab_equipment(Base):
  __tablename__ = "lab_equipments" 
  id = Column(Integer, nullable=False)
  laboratory_id = Column(Integer, ForeignKey("laboratories.id"))
  user_id = Column(Integer, nullable=False)
  sensors = relationship("Sensor", backref="lab_equipment")
    
  def __init__(self) -> None:
       pass
    

class Sensor(Base):
  __tablename__ = "sensors" 
  id = Column(Integer, nullable=False)
  topic = Column(String(255), nullable=False)
  lab_equipments_id = Column(Integer, ForeignKey("lab_equipments.id"))
  process_data_records = relationship("Process_data_record", backref="sensor")
    
  def __init__(self, topic) -> None:
    self.topic = topic
    
    

class Dashboard(Base):
  __tablename__ = "dashboards" 
  id = Column(Integer, nullable=False)
  resource_id = Column(String(255), nullable=False)
  author_id = Column(Integer, ForeignKey("users.id"))
  created_at = Column(DateTime, nullable=False)
    
  def __init__(self, created_at) -> None:
    self.created_at = created_at
    
    

class Laboratorie(Base):
  __tablename__ = "laboratories" 
  id = Column(Integer, nullable=False)
  name = Column(String(255), nullable=False)
  location = Column(String(255), nullable=False)
  users = relationship("User", backref="laboratorie")
  lab_equipments = relationship("Lab_equipment", backref="laboratorie")
    
  def __init__(self, name, location) -> None:
    self.name = name
    self.location = location
    
    

class Process_data_record(Base):
  __tablename__ = "process_data_records" 
  id = Column(Integer, nullable=False)
  recording_from = Column(DateTime, nullable=False)
  recording_to = Column(DateTime, nullable=False)
  sensor_id = Column(Integer, ForeignKey("sensors.id"))
    
  def __init__(self, recording_from, recording_to) -> None:
    self.recording_from = recording_from
    self.recording_to = recording_to
    
    