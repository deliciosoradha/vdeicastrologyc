from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    report_data = Column(JSON)
    pdf_path = Column(String)
    is_paid = Column(Boolean, default=False)
    payment_id = Column(String)
    created_at = Column(DateTime, server_default='now()')
    updated_at = Column(DateTime, onupdate='now()')

    user = relationship("User", back_populates="reports")

    def __repr__(self):
        return f"<Report(user_id={self.user_id}, is_paid={self.is_paid})>"
