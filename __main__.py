import os,json,sys

def main():
    print("Welcome to ChromeExtensionsSetupTools!")
    print("select options...\nn: new extensions(default)\nq: quit\n")
    op = input("> ")
    name="sample_extension"
    description=""
    manifest_version=3
    version = ""
    def zero_ignore_input(prompt:str,default):
        """
        Args:
            prompt(str): The title that will be displayed in the console.
            default(Any): This is the default value returned if no input is given.
        """
        arg = input(prompt)
        if len(arg) == 0:
            return default
        else:
            return arg
    if op == "n" or op == "":
        try:
            name = zero_ignore_input(f"Type extension name ({name}) > ",name)
            discription = zero_ignore_input("Type extension discription () > ","")
            version = zero_ignore_input("Type extension version (1.0.0) > ","1.0.0")
            try:
                manifest_version = int(zero_ignore_input("Type extension manifest_version (3) > ",3))
            except ValueError:
                print("Error!: manifest_version must be an integer.")
                sys.exit()
        except KeyboardInterrupt:
            print("exit.")
            sys.exit()
        except Exception as e:
            print(f"Error!: {e}")
        manifest_json = {
            "name":name,
            "description":description,
            "version":version,
            "manifest_version":manifest_version
        }
        if not os.path.exists(f"./{name}/"):
            os.makedirs(f"{name}")
        else:
            print(f"A project called \"{name}\" already exists")
            sys.exit()
        with open(os.path.join(f"{name}","manifest.json"), 'w',encoding="utf-8") as file:
            file.write(json.dumps(manifest_json, indent=4,ensure_ascii = False))
        print("complete!")
if __name__ == "__main__":
    main()