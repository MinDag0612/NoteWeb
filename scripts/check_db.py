from backend.app.core.database import connDB


def main():
    try:
        result = connDB.client.admin.command("ping")

        if result.get("ok") == 1:
            print("MongoDB is running and connection is successful.")

    except Exception as exc:
        print(f"MongoDB connection failed: {exc}")
        raise SystemExit(1)

    finally:
        connDB.client.close()


if __name__ == "__main__":
    main()
