from dataclasses import dataclass, field
import datetime


@dataclass
class ChangeItem:
    ItemNumber: int
    text: str
    attachment: str = None  # Приложение может быть необязательным


@dataclass
class AgreementTemplate:
    contract_number: int
    contract_date: datetime.date
    contract_topic: str
    customer_full_name: str
    supplier_full_name: str
    customer_executive_name: str
    supplier_executive_name: str
    city: str
    date: datetime.date
    changes: list[ChangeItem] = field(default_factory=list)
    attachments: list[AttachmentItem] = field(default_factory=list)

    HeaderTemplate: str = """
    ДОПОЛНИТЕЛЬНОЕ СОГЛАШЕНИЕ № УКАЖИТЕ_НОМЕР_СОГЛАШЕНИЯ
    к Государственному контракту от {{ contract_date }} № {{ contract_number }}
    {{ contract_topic }}
    """

    PreambulaTemplate: str = """
    {{ city }}                                                                 «____»   ___________ 2024 г.
    {{ customer_full_name }}, именуемая в дальнейшем «Заказчик», в лице {{ customer_executive_name }}, с одной стороны,
    и {{ supplier_full_name }}, именуемый в дальнейшем «Поставщик», в лице {{ supplier_executive_name }}, с другой стороны, 
    вместе именуемые «Стороны», заключили Дополнительное соглашение.
    """

    Changes: list[ChangeItem] = field(default_factory=list)  # Список изменений, по умолчанию пустой

    FooterTemplate: str = """
    ПОДПИСИ СТОРОН:

    ЗАКАЗЧИК:
    {{ customer_full_name }}

    ПОСТАВЩИК:
    {{ supplier_full_name }}

    _________________/{{ customer_executive_name }}
    м.п.

    _________________/ {{ supplier_executive_name }}
    м.п.
    """

    def __init__(
        self,
        contract_number: str,
        contract_date: datetime.date,
        contract_topic: str,
        customer_full_name: str,
        supplier_full_name: str,
        customer_executive_name: str,
        supplier_executive_name: str,
        city: str,
        changes: list[ChangeItem] = None,
        attachments: list[str] = None
    ):
        """Инициализация шаблона дополнительного соглашения с данными"""
        self.contract_number = contract_number
        self.contract_date = contract_date
        self.contract_topic = contract_topic
        self.customer_full_name = customer_full_name
        self.supplier_full_name = supplier_full_name
        self.customer_executive_name = customer_executive_name
        self.supplier_executive_name = supplier_executive_name
        self.city = city
        self.date = datetime.date.today()
        self.changes = changes if changes else []
        self.attachments = attachments if attachments else []

    def generate_agreement(self):
        """Генерация текста дополнительного соглашения на основе шаблона."""
        header = self.HeaderTemplate.format(
            agreement_number=self.agreement_number,
            contract_date=self.contract_date,
            contract_number=self.contract_number,
            contract_topic=self.contract_topic
        )

        preambula = self.PreambulaTemplate.format(
            city=self.city,
            customer_full_name=self.customer_full_name,
            supplier_full_name=self.supplier_full_name,
            customer_fio=self.customer_executive_name
        )

        # Генерация списка изменений
        changes_text = "\n".join(
            [f"{change.ItemNumber}. {change.text} {f'Приложение: {change.attachment}' if change.attachment else ''}" for change in self.changes])

        footer = self.FooterTemplate.format(
            customer_fio=self.customer_executive_name,
            supplier_fio=self.supplier_full_name
        )

        return f"{header}\n\n{preambula}\n\n{changes_text}\n\n{footer}"

# execute this file here
agreement_template = AgreementTemplate(.....)
return agreement_template.generate_agreement()