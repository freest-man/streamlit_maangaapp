# streamlit_maangaapp

This Streamlit app is a simple yet powerful tool to visualize historical data for selected stocks. 

Let's break down the code step by step:


Here, the required libraries are imported:

- **`yfinance`**: A library for fetching financial data, used to get stock data.
- **`streamlit`**: The Streamlit library for creating interactive web applications.
- **`pandas`**: A versatile library for data manipulation and analysis.


## Sidebar for user input features
st.sidebar.header('Select Stock')


The **`st.sidebar`** object is used to create a sidebar in the app. The **`header`** method is used to add a title to the sidebar, and it reads "Select Stock."

```

def get_user_selected_stock():
    selected_stock = st.sidebar.selectbox('Choose Stock', ('GOOGL', 'AAPL', 'AMZN', 'NFLX', 'META'))
    return selected_stock

```

A function **`get_user_selected_stock`** is defined to get the user's choice of stock. It uses **`st.sidebar.selectbox`** to create a dropdown menu in the sidebar with options ('GOOGL', 'AAPL', 'AMZN', 'NFLX', 'META'). The selected stock is then returned.

```

# Get user input
ticker_symbol = get_user_selected_stock()

```

The selected stock is obtained by calling the function **`get_user_selected_stock`**.

```

# Display selected stock information
st.write(f"Displaying historical data for {ticker_symbol} stock:")
st.write("Closing price and volume trends:")

```

Using **`st.write`**, the app displays information about the selected stock in the main content area. It shows the stock's symbol and a message about the displayed data.


```

# Get data on the selected ticker
ticker_data = yf.Ticker(ticker_symbol)

```

**`yf.Ticker`** is used to create a Ticker object for the selected stock, enabling the retrieval of stock-related data.


```

# Get historical trends for the selected ticker
historical_data = ticker_data.history(period='1d', start='2010-5-31', end='2024-1-1')

```

The app fetches historical data for the selected stock using the **`history`** method of the Ticker object. In this case, it fetches daily data (**`period='1d'`**) from May 31, 2010, to January 1, 2024.


```
# Display closing price trends
st.write("## Closing Price")
st.line_chart(historical_data.Close)

```

The closing price trends are displayed with a heading using **`st.write("## Closing Price")`**, and the line chart is created using **`st.line_chart`** with the closing price data.


```
# Display volume trends
st.write("## Volume")
st.line_chart(historical_data.Volume)

```

Similarly, the volume trends are displayed with a heading, and the line chart is created using the volume data.

This Streamlit app allows users to select a stock from a sidebar, and it dynamically fetches and displays historical closing prices and volume trends for the chosen stock. 

The visualizations are presented in a user-friendly and interactive way, making it easy for users to explore stock data.
