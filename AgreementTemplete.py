from dataclasses import dataclass, field
import datetime

@dataclass
class ChangeItem:
    ItemNumber: int
    text: str
    attachment: str = None  # Приложение может быть необязательным

@dataclass
class AgreementTemplate:
    HeaderTemplate: str = """
    ДОПОЛНИТЕЛЬНОЕ СОГЛАШЕНИЕ № {{ agreement_number }}
    к Государственному контракту от {{ contract_date }} № {{ contract_number }}
    {{ contract_topic }}
    """
    
    PreambulaTemplate: str = """
    {{ city }}                                                                 «____»   ___________ 2024 г.
    {{ customer_preamble }}, именуемая в дальнейшем «Заказчик», в лице {{ customer_chief_preamble }} {{ customer_fio }}, 
    действующего на основании {{ regulatory_customer_documents_preamble }}, с одной стороны, и {{ supplier_chief_preamble }} 
    {{ supplier_fio }}, именуемый в дальнейшем «Поставщик», в лице {{ supplier_fio }}, действующего на основании 
    {{ regulatory_supplier_documents_preamble }}, с другой стороны, вместе именуемые «Стороны», заключили Дополнительное соглашение.
    """

    Changes: list[ChangeItem] = field(default_factory=list)  # Список изменений, по умолчанию пустой
    
    FooterTemplate: str = """
    ПОДПИСИ СТОРОН:
    
    ЗАКАЗЧИК:
    {{ customer_preamble }}

    ПОСТАВЩИК:                                                    
    {{ supplier_chief_preamble }}
    {{ supplier_fio }}

    _________________/{{ customer_fio }}/ 
    м.п.

    _________________/ {{ supplier_fio }} /
    м.п.
    """

    Name: str
    Date: datetime.date
    AgreementNumber: int
    ContractNumber: int
    ContractDate: datetime.date
    ContractTopic: str
    CustomerPreamble: str
    SupplierPreamble: str
    City: str
    Attachments: list[str] = field(default_factory=list)  # Приложения

    def __init__(self, name: str, agreement_number: int, contract_number: int, contract_date: datetime.date, contract_topic: str, customer_preamble: str, supplier_preamble: str, city: str, date: datetime.date = None, changes: list[ChangeItem] = None, attachments: list[str] = None):
        """Инициализация шаблона дополнительного соглашения с данными"""
        self.Name = name
        self.AgreementNumber = agreement_number
        self.ContractNumber = contract_number
        self.ContractDate = contract_date
        self.ContractTopic = contract_topic
        self.CustomerPreamble = customer_preamble
        self.SupplierPreamble = supplier_preamble
        self.City = city
        self.Date = date if date else datetime.date.today()  # Установка даты, если не указана
        self.Changes = changes if changes else []
        self.Attachments = attachments if attachments else []

    def generate_agreement(self):
        """Генерация текста дополнительного соглашения на основе шаблона."""
        header = self.HeaderTemplate.format(
            agreement_number=self.AgreementNumber,
            contract_date=self.ContractDate,
            contract_number=self.ContractNumber,
            contract_topic=self.ContractTopic
        )

        preambula = self.PreambulaTemplate.format(
            city=self.City,
            customer_preamble=self.CustomerPreamble,
            supplier_preamble=self.SupplierPreamble,
            customer_fio=self.Name
        )

        # Генерация списка изменений
        changes_text = "\n".join([f"{change.ItemNumber}. {change.text} {f'Приложение: {change.attachment}' if change.attachment else ''}" for change in self.Changes])

        footer = self.FooterTemplate.format(
            customer_fio=self.Name,
            supplier_fio=self.SupplierPreamble
        )

        return f"{header}\n\n{preambula}\n\n{changes_text}\n\n{footer}"
