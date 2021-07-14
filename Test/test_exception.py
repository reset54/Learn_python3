#
try:
    data = [{"name": "Пётр", "phone": "123"}, {"name": "Иван"}]
    print(data[0]["last"])

except ZeroDivisionError:
    print("ZeroDivisionError")
except IndexError:
    print("IndexError")
except SyntaxError:
    print("SyntaxError")
except KeyError:
    print("KeyError")
except TypeError:
    print("TypeError")
except NameError:
    print("NameError")
except Exception:
    print("Exception")