from abc import ABC, abstractmethod

# Single Responsibility: каждый класс выполняет одну задачу

class ReportGenerator:
    """Генерирует отчет"""
    def generate(self, data):
        return f"Отчет по данным: {data}"

class FileSaver:
    """Сохраняет данные в файл"""
    def save_to_file(self, content, filename):
        with open(filename, 'w') as f:
            f.write(content)

# Open-Closed: классы открыты для расширения (через наследование), но закрыты для изменений
class Notifier(ABC):
    """Интерфейс для отправки уведомлений"""
    @abstractmethod
    def notify(self, message):
        pass

class EmailNotifier(Notifier):
    def notify(self, message):
        print(f"Отправка Email: {message}")

class SMSNotifier(Notifier):
    def notify(self, message):
        print(f"Отправка SMS: {message}")

# Liskov Substitution: наследники Notifier могут заменять базовый класс
def send_alert(notifier: Notifier, message: str):
    notifier.notify(message)

# Interface Segregation: нет одного универсального интерфейса, разделено на небольшие
class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Savable(ABC):
    @abstractmethod
    def save(self):
        pass

class Document(Printable, Savable):
    def print(self):
        print("Печать документа...")

    def save(self):
        print("Сохранение документа...")

# Dependency Inversion: зависимости инъектируются через абстракции
class App:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def process(self):
        self.notifier.notify("Процесс завершен успешно!")

# Демонстрация
if __name__ == "__main__":
    # Single Responsibility
    report = ReportGenerator().generate("Продажи за май")
    FileSaver().save_to_file(report, "report.txt")

    # Open-Closed + Liskov
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()
    send_alert(email_notifier, "Важное сообщение")
    send_alert(sms_notifier, "Срочное уведомление")

    # Interface Segregation
    doc = Document()
    doc.print()
    doc.save()

    # Dependency Inversion
    app = App(notifier=email_notifier)
    app.process()
