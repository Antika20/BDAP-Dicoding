import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime
from babel.numbers import format_currency
from pathlib import Path
sns.set(style='dark')


def create_season_bs(day_df):
    byseason_df = day_df.groupby(by="season").instant.nunique().reset_index()
    byseason_df.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return byseason_df


def create_yr_bs(day_df):
    yr_df = day_df.groupby(by="yr").instant.nunique().reset_index()
    yr_df.rename(columns={
        "instant": "sum"
    }, inplace=True)
    return yr_df


def create_holiday_bs(df):
    holiday_df = df.groupby(by="holiday").instant.nunique().reset_index()
    holiday_df.rename(columns={
        "instant": "sum"
    }, inplace=True)
    return holiday_df


def create_workingDay_bs(df):
    workingDay_df = df.groupby(by="workingday").instant.nunique().reset_index()
    workingDay_df.rename(columns={
        "instant": "sum"
    }, inplace=True)
    return workingDay_df


def create_weather_bs(df):
    weather_df = df.groupby(by="weathersit").instant.nunique().reset_index()
    weather_df.rename(columns={
        "instant": "sum"
    }, inplace=True)
    return weather_df


def sidebar(df):
    df["dteday"] = pd.to_datetime(df["dteday"])
    min_date = df["dteday"].min()
    max_date = df["dteday"].max()

    with st.sidebar:
        st.image("https://raw.githubusercontent.com/anddfian/Dicoding-BADP/main/Submission/dashboard/Capital Bikeshare Logo.png")

        def on_change():
            st.session_state.date = date

        date = st.date_input(
            label="Rentang Waktu",
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date],
            on_change=on_change
        )

    return date


def season_bs(df):
    st.subheader("Season  Trend Bike Sharing")

    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        x="season",
        y="sum",
        data=df.sort_values(by="season", ascending=False),
        ax=ax,

    )
    ax.set_title("Number of Bike Sharing by Season", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=25)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)


def year_bs(df):
    st.subheader("Year Trend Bike Sharing")

    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        x="yr",
        y="sum",
        data=df.sort_values(by="yr", ascending=False),
        ax=ax,

    )
    ax.set_title("Number of Bike Sharing by Year", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=25)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)


def month_bs(df):
    st.subheader("Month Trend Bike Sharing")

    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        x="mnth",
        y="cnt",
        data=df.sort_values(by="mnth", ascending=False),
        ax=ax,

    )
    ax.set_title("Number of Bike Sharing by Month", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=25)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)


def holiday_bs(df):
    st.subheader("Holiday Trend  Bike Sharing")

    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        x="holiday",
        y="sum",
        data=df.sort_values(by="holiday", ascending=False),
        ax=ax,

    )
    ax.set_title("Number of Bike Sharing by Holiday",
                 loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=25)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)


def workingDay_bs(df):
    st.subheader("Working Day Trend  Bike Sharing")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="workingday",
        y="sum",
        data=df.sort_values(by="workingday", ascending=False),
        ax=ax
    )
    ax.set_title("Number of Bike Sharing by Working Day",
                 loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)


def weather_bs(df):
    st.subheader("Weather Bike Sharing")

    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        x="weathersit",
        y="sum",
        data=df.sort_values(by="weathersit", ascending=False),
        ax=ax
    )
    ax.set_title("Number of Bike Sharing by Weather Sit",
                 loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)


if __name__ == "__main__":
    sns.set(style="dark")

    st.header("Bike Sharing Dashboard :bike:")

    day_df_csv = Path(__file__).parents[1] / \
        'Submission/clean_bike_sharing2.csv'

    day_df = pd.read_csv(day_df_csv)

    date = sidebar(day_df)
    if(len(date) == 2):
        main_df = day_df[(day_df["dteday"] >= str(date[0])) &
                         (day_df["dteday"] <= str(date[1]))]
    else:
        main_df = day_df[(day_df["dteday"] >= str(st.session_state.date[0])) & (
            day_df["dteday"] <= str(st.session_state.date[1]))]

    season_df = create_season_bs(main_df)
    season_bs(season_df)
    year_df = create_yr_bs(main_df)
    year_bs(year_df)
    month_bs(main_df)
    holiday_df = create_holiday_bs(main_df)
    holiday_bs(holiday_df)
    workingday_df = create_workingDay_bs(main_df)
    workingDay_bs(workingday_df)

    weathersit_df = create_weather_bs(main_df)
    weather_bs(weathersit_df)

    year_copyright = datetime.date.today().year
    copyright = "Copyright © " + str(year_copyright) + " | Bike Sharing Dashboard | All Rights Reserved | " + \
        "Made with :heart: by [@Antika](https://www.linkedin.com/in/antika-orinda-53b7981ba/)"
    st.caption(copyright)
