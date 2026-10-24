from dataclasses import dataclass

@dataclass
class Statistics:
    visitors_count: int
    ticket_normal_count: int
    ticket_vip_count: int
    ticket_premium_count: int
    average_age: int
