/*
Created By:    Zachary Ordo
Created Date:  2021-08-05
Last Modified: 2022-02-10

This job builds the Site Energy Usage table for the Clearfork Plant.
*/

SET NOCOUNT ON
DECLARE @StartDate DateTime
DECLARE @EndDate DateTime
SET @StartDate = '2021-08-31 11:00:00'
SET @EndDate = DateAdd(day, DateDiff(day, 0, GetDate()), 1)
SET NOCOUNT OFF
INSERT INTO [GISViews].[dbo].[CFHISSVR02AnalogHisEnergy] (TagName, Description, DateTime, ActualDate, ActualYear, ActualQuarter, ActualMonth, ActualMonthNumber, ActualDay, Value, Units)
	SELECT * FROM (
	SELECT TagName,
	CASE TagName
			WHEN '138KV_BKR1\RealEnerg' THEN 'Site Energy (138 kV Breaker 1 / 2)'
			WHEN '138KV_BKR2\RealEnerg' THEN 'Site Energy (138 kV Breaker 2 / 2)'
		END AS Description,
	DateTime,
	CONVERT(date, DATEADD(dd,1,DateTime)) as ActualDate,
	YEAR(CONVERT(date, DATEADD(dd,1,DateTime))) as ActualYear,
	DATENAME(quarter, CONVERT(date, DATEADD(dd,1,DateTime))) as ActualQuarter,
	DATENAME(month, CONVERT(date, DATEADD(dd,1,DateTime))) as ActualMonth,
	MONTH(CONVERT(date, DATEADD(dd,1,DateTime))) as ActualMonthNumber,
	DAY(CONVERT(date, DATEADD(dd,1,DateTime))) as ActualDay,
	Value,
	CASE TagName
			WHEN '138KV_BKR1\RealEnerg' THEN 'MWh'
			WHEN '138KV_BKR2\RealEnerg' THEN 'MWh'
		END AS Units
		FROM [CFHISSVR02].[Runtime].[dbo].[History]
		WHERE TagName IN ('138KV_BKR1\RealEnerg','138KV_BKR2\RealEnerg')
		AND wwRetrievalMode = 'counter'
		AND wwResolution = 86400000
		AND wwQualityRule = 'optimistic'
		AND wwTimeStampRule = 'start'
		AND DateTime >= @StartDate
		AND DateTime <= @EndDate) temp
	WHERE temp.Value IS NOT NULL
	AND temp.ActualDate <> '2020-09-13';