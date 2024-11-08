from abc import ABC, abstractmethod

# 定义一个抽象基类 Button，它定义了一个抽象方法 click
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

# 定义一个抽象基类 CheckBox，它定义了一个抽象方法 check
class CheckBox(ABC):
    @abstractmethod
    def check(self):
        pass

# 定义一个具体类 WindowsButton，它继承自 Button，并实现了 click 方法
class WindowsButton(Button):
    def click(self) -> str:
        return "windows click"

# 定义一个具体类 WindowsCheckBox，它继承自 CheckBox，并实现了 check 方法
class WindowsCheckBox(CheckBox):
    def check(self) -> str:
        return "windows checkbox"

# 定义一个具体类 MacOSButton，它继承自 Button，并实现了 click 方法
class MacOSButton(Button):
    def click(self) -> str:
        return "MacOS click"

# 定义一个具体类 MacOSCheckBox，它继承自 CheckBox，并实现了 check 方法
class MacOSCheckBox(CheckBox):
    def check(self) -> str:
        return "MacOS checkbox"

# 定义一个抽象基类 GuiFactory，它定义了 create_button 和 create_checkbox 方法
class GuiFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# 定义一个具体类 WindowsFactory，它继承自 GuiFactory，并实现了 create_button 和 create_checkbox 方法
class WindowsFactory(GuiFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckBox()

# 定义一个具体类 MacOSFactory，它继承自 GuiFactory，并实现了 create_button 和 create_checkbox 方法
class MacOSFactory(GuiFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckBox()

# 定义一个工厂函数 CreateGui，它接受一个 GuiFactory 对象作为参数，并使用该工厂创建 button 和 checkbox 对象
def CreateGui(factory: GuiFactory):
    button = factory.create_button()
    check = factory.create_checkbox()
    return button, check

# 创建 WindowsFactory 和 MacOSFactory 对象
wf = WindowsFactory()
mf = MacOSFactory()

# 使用 CreateGui 函数创建 Windows 的 button 和 checkbox 对象
button, check = CreateGui(wf)
print(button.click())
print(check.check())

# 使用 CreateGui 函数创建 MacOS 的 button 和 checkbox 对象
button, check = CreateGui(mf)
print(button.click())
print(check.check())