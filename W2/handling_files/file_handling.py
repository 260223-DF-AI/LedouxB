def main():
    print("Hello, World!")

    sample_data = """Name,Age,City,
Benjamin,23,Atkinson,
McKenzie,25,Tewksbury,
Sage,26,Lawrence,
"""



    try:
        with open("data/sample.csv", 'w', encoding='utf-8') as file:
            file.write(sample_data)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        if not file.closed:
            file.close()
    """
    try:
        with open("data/sample.csv", 'r', encoding='utf-8') as file:
            content = file.read()
            # print(content)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        if not file.closed:
            file.close()
    """

    try:
        with open("data/sample.csv", 'r', encoding='utf-8') as f:
            records = []
            for i, l in enumerate(f):
                if i == 0:
                    continue
                line = l.split(',')[:-1]
                records.append({
                "name": line[0],
                "age": line[1],
                "city": line[2],
            })
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        if not f.closed:
            f.close()

def save_reports(data, filename: str):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # f.write(data)
            pass
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        if not f.closed:
            f.close()


if __name__ == "__main__":
    main()