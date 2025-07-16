import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import spearmanr
from scipy.stats import chi2_contingency
from statsmodels.tools import add_constant
from statsmodels.stats.outliers_influence import variance_inflation_factor

import streamlit as st

def custom_md(text):
    st.markdown(f"<div class='custom-base custom-markdown'>{text}</div>", unsafe_allow_html=True)
def custom_title(text):
    st.markdown(f"<h3 class='custom-base custom-title'>{text}</h3>", unsafe_allow_html=True)

def av(data):
    
    
    
def mileage_effect_car_prices(data):
    # Plotting Graph
    plt.figure(figsize=(10,6))

    # Putting Data and Plotting Trend
    sns.regplot(data=data, x="mileage_kmpl", y="price_usd", scatter_kws={"alpha":0.5}, line_kws={"color" : "red"})

    # Titles and Labels
    plt.title("Car Mileage vs Used Car Prices", fontsize=18)
    plt.xlabel("Mileage (kmpl)")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.tight_layout()
    
    # Calculate Spearman correlation
    corr, pval = stats.spearmanr(data["mileage_kmpl"], data["price_usd"])
    st.markdown(f"**Spearman Correlation: {corr:.2f} (p = {pval:.4f})**")
    
    st.pyplot(plt)
    
def accidents_vs_prices(data):
    plt.figure(figsize=(10, 6))

    # Scatter plot with regression line
    sns.regplot(data=data, x="accidents_reported", y="price_usd", scatter_kws={'alpha':0.5}, line_kws={"color": "red"})
    plt.title("Correlation Between Number of Accidents and Price")
    plt.xlabel("Number of Accidents Reported")
    plt.ylabel("Car Price (USD)")

    # Calculate Spearman correlation
    corr, pval = stats.spearmanr(data["accidents_reported"], data["price_usd"])
    st.markdown(f"**Spearman Correlation: {corr:.2f} (p = {pval:.4f})**")

    st.pyplot(plt)

def avg_price_by_fuel_type(data) :
    avg_prices_fuel = data.groupby("fuel_type")["price_usd"].mean().sort_values(ascending=False)
    
    # Plotting Graph
    plt.figure(figsize=(12,6))

    # Color coding
    norm = plt.Normalize(avg_prices_fuel.min(), avg_prices_fuel.max())
    colors = plt.cm.coolwarm(norm(avg_prices_fuel.values))

    bars = plt.bar(avg_prices_fuel.index, avg_prices_fuel.values, color=colors)

    # Listing the actual average prices
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 20, f"{yval:,.0f}", ha = "center", va = "bottom", fontsize=9)

    # Titles / Labels
    plt.title("Average Used Car Prices by Fuel Type", fontsize=18)
    plt.ylabel("Average Prices (USD)")
    plt.xlabel("Fuel Type")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.tight_layout()
    st.pyplot(plt)
    
    # Table
    st.subheader("Table")
    styled_table = avg_prices_fuel.round(0).to_frame().style.format("${:,.0f}").highlight_max(props='font-weight: bold; background-color: gold; color: black')
    st.dataframe(styled_table)

def price_by_age(data):
    plt.figure(figsize=(10,6))
    sns.regplot(data=data, x="make_year", y="price_usd", scatter_kws={"alpha":0.5}, line_kws={"color" : "red"})
    plt.title("Used Car Prices based on Make Year", fontsize=18)
    plt.xlabel("Year of Make")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)

def popularity_brand(data):
    plt.figure(figsize=(12,6))
    brand_order = data["brand"].value_counts().index

    sns.countplot(data=data,x="brand", order=brand_order, palette="viridis")
    plt.title("Popularity of Used Car Brands", fontsize=18)
    plt.xlabel("Brand")
    plt.ylabel("Number of Listings")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

def popularity_color(data):
    # Define palette matching the actual car colors
    custom_palette = {
        "Blue": "blue",
        "Silver": "silver",
        "Gray": "gray",
        "White": "white",
        "Red": "red",
        "Black": "black"
    }

    plt.figure(figsize=(10, 6))
    sns.countplot(
        data=data,
        x="color",
        hue="color",
        order=data["color"].value_counts().index,
        palette=custom_palette,
        edgecolor="black",
        legend=False
    )
    plt.title("Popularity of Car Colors", fontsize=18)
    plt.xlabel("Color")
    plt.ylabel("Number of Cars")
    plt.ylim(1500,2000)
    plt.grid(axis="y")
    plt.tight_layout()
    st.pyplot(plt)

