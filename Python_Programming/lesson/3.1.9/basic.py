try:
    # Risky code
    pass

except ValueError:
    # Handle invalid value
    pass

except ZeroDivisionError:
    # Handle division by zero
    pass

except Exception as e:
    # Handle other unexpected errors
    print("Error:", e)

else:
    # Runs if no error occurred
    pass

finally:
    # Always runs
    pass


# flow - try -> except -> else -> finally
