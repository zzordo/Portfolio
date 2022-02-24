﻿/*
Created By:    Zachary Ordo
Created Date:  2021-08-05
Last Modified: 2022-02-10

This job builds the Delivery Point Component Summary table for the Clearfork Plant.
*/

SET NOCOUNT ON
DECLARE @StartDate DateTime
DECLARE @EndDate DateTime
SET @StartDate = '08/31/2020 11:01'
SET @EndDate = DateAdd(day, DateDiff(day, 0, GetDate()), 1)
SET NOCOUNT OFF
INSERT INTO [GISViews].[dbo].[CFHISSVR02AnalogHisComps] (TagName, Description, chemFormula, rptPriority, StartDateTime, DateTime, ActualDate, ActualYear, ActualQuarter, ActualMonth, ActualMonthNumber, ActualDay, Value, vValue)
	SELECT * FROM (
	SELECT TagName,
	CASE TagName
			WHEN 'GC1_INLET_BTU' THEN 'BTU/SCF'
			WHEN 'GC1_INLET_C1' THEN 'C1'
			WHEN 'GC1_INLET_C2' THEN 'C2'
			WHEN 'GC1_INLET_C2PLUS_GAL' THEN 'C2+ gal/mcf'
			WHEN 'GC1_INLET_C3' THEN 'C3'
			WHEN 'GC1_INLET_C3PLUS_GAL' THEN 'C3+ gal/mcf'
			WHEN 'GC1_INLET_C6_PLUS' THEN 'C6+'
			WHEN 'GC1_INLET_CO2' THEN 'CO2'
			WHEN 'GC1_INLET_IC4' THEN 'IC4'
			WHEN 'GC1_INLET_IC5' THEN 'IC5'
			WHEN 'GC1_INLET_N2' THEN 'N2'
			WHEN 'GC1_INLET_NC4' THEN 'NC4'
			WHEN 'GC1_INLET_NC5' THEN 'NC5'
			WHEN 'GC1_INLET_SGU' THEN 'SGU'
			WHEN 'GC1_RESIDUE_BTU' THEN 'BTU/SCF'
			WHEN 'GC1_RESIDUE_C1' THEN 'C1'
			WHEN 'GC1_RESIDUE_C2' THEN 'C2'
			WHEN 'GC1_RESIDUE_C2_RECOVER' THEN 'C2 Recovery %'
			WHEN 'GC1_RESIDUE_C3' THEN 'C3'
			WHEN 'GC1_RESIDUE_C3_RECOVER' THEN 'C3 Recovery %'
			WHEN 'GC1_RESIDUE_C6_PLUS' THEN 'C6+'
			WHEN 'GC1_RESIDUE_CO2' THEN 'CO2'
			WHEN 'GC1_RESIDUE_IC4' THEN 'IC4'
			WHEN 'GC1_RESIDUE_IC5' THEN 'IC5'
			WHEN 'GC1_RESIDUE_N2' THEN 'N2'
			WHEN 'GC1_RESIDUE_NC4' THEN 'NC4'
			WHEN 'GC1_RESIDUE_NC5' THEN 'NC5'
			WHEN 'GC1_RESIDUE_REL_DENS' THEN 'REL DENS'
			WHEN 'GC2_YGRADE_C1' THEN 'C1'
			WHEN 'GC2_YGRADE_C2' THEN 'C2'
			WHEN 'GC2_YGRADE_C2_LIQ_VOL' THEN 'GC2_YGRADE_C2_LIQ_VOL'
			WHEN 'GC2_YGRADE_C2C3_RATIO' THEN 'C2/C3 RATIO NGL'
			WHEN 'GC2_YGRADE_C3' THEN 'C3'
			WHEN 'GC2_YGRADE_C6_PLUS' THEN 'C6+'
			WHEN 'GC2_YGRADE_IC4' THEN 'IC4'
			WHEN 'GC2_YGRADE_IC5' THEN 'IC5'
			WHEN 'GC2_YGRADE_NC4' THEN 'NC4'
			WHEN 'GC2_YGRADE_NC5' THEN 'NC5'
		END AS Description,
	CASE TagName
			WHEN 'GC1_INLET_BTU' THEN 'BTU/SCF'
			WHEN 'GC1_INLET_C1' THEN N'C₁'
			WHEN 'GC1_INLET_C2' THEN N'C₂'
			WHEN 'GC1_INLET_C2PLUS_GAL' THEN N'C₂+ gal/mcf'
			WHEN 'GC1_INLET_C3' THEN N'C₃'
			WHEN 'GC1_INLET_C3PLUS_GAL' THEN N'C₃+ gal/mcf'
			WHEN 'GC1_INLET_C6_PLUS' THEN N'C₆+'
			WHEN 'GC1_INLET_CO2' THEN N'CO₂'
			WHEN 'GC1_INLET_IC4' THEN N'IC₄'
			WHEN 'GC1_INLET_IC5' THEN N'IC₅'
			WHEN 'GC1_INLET_N2' THEN N'N₂'
			WHEN 'GC1_INLET_NC4' THEN N'NC₄'
			WHEN 'GC1_INLET_NC5' THEN N'NC₅'
			WHEN 'GC1_INLET_SGU' THEN 'SGU'
			WHEN 'GC1_RESIDUE_BTU' THEN 'BTU/SCF'
			WHEN 'GC1_RESIDUE_C1' THEN  N'C₁'
			WHEN 'GC1_RESIDUE_C2' THEN  N'C₂'
			WHEN 'GC1_RESIDUE_C2_RECOVER' THEN  N'C₂ Recovery %'
			WHEN 'GC1_RESIDUE_C3' THEN N'C₃'
			WHEN 'GC1_RESIDUE_C3_RECOVER' THEN N'C₃ Recovery %'
			WHEN 'GC1_RESIDUE_C6_PLUS' THEN N'C₆+'
			WHEN 'GC1_RESIDUE_CO2' THEN N'CO₂'
			WHEN 'GC1_RESIDUE_IC4' THEN N'IC₄'
			WHEN 'GC1_RESIDUE_IC5' THEN N'IC₅'
			WHEN 'GC1_RESIDUE_N2' THEN N'N₂'
			WHEN 'GC1_RESIDUE_NC4' THEN N'NC₄'
			WHEN 'GC1_RESIDUE_NC5' THEN N'NC₅'
			WHEN 'GC1_RESIDUE_REL_DENS' THEN 'REL DENS'
			WHEN 'GC2_YGRADE_C1' THEN N'C₁'
			WHEN 'GC2_YGRADE_C2' THEN N'C₂'
			WHEN 'GC2_YGRADE_C2_LIQ_VOL' THEN 'GC2_YGRADE_C2_LIQ_VOL'
			WHEN 'GC2_YGRADE_C2C3_RATIO' THEN N'C₂/C₃ RATIO NGL'
			WHEN 'GC2_YGRADE_C3' THEN N'C₃'
			WHEN 'GC2_YGRADE_C6_PLUS' THEN N'C₆+'
			WHEN 'GC2_YGRADE_IC4' THEN N'IC₄'
			WHEN 'GC2_YGRADE_IC5' THEN N'IC₅'
			WHEN 'GC2_YGRADE_NC4' THEN N'NC₄'
			WHEN 'GC2_YGRADE_NC5' THEN N'NC₅'
		END AS chemFormula,
	CASE TagName
			WHEN 'GC1_INLET_BTU' THEN 11
			WHEN 'GC1_INLET_C1' THEN 3
			WHEN 'GC1_INLET_C2' THEN 4
			WHEN 'GC1_INLET_C2PLUS_GAL' THEN 12
			WHEN 'GC1_INLET_C3' THEN 5
			WHEN 'GC1_INLET_C3PLUS_GAL' THEN 13
			WHEN 'GC1_INLET_C6_PLUS' THEN 10
			WHEN 'GC1_INLET_CO2' THEN 2
			WHEN 'GC1_INLET_IC4' THEN 6
			WHEN 'GC1_INLET_IC5' THEN 8
			WHEN 'GC1_INLET_N2' THEN 1
			WHEN 'GC1_INLET_NC4' THEN 7
			WHEN 'GC1_INLET_NC5' THEN 9
			WHEN 'GC1_INLET_SGU' THEN 14
			WHEN 'GC1_RESIDUE_BTU' THEN 11
			WHEN 'GC1_RESIDUE_C1' THEN 3
			WHEN 'GC1_RESIDUE_C2' THEN 4
			WHEN 'GC1_RESIDUE_C2_RECOVER' THEN 13
			WHEN 'GC1_RESIDUE_C3' THEN 5
			WHEN 'GC1_RESIDUE_C3_RECOVER' THEN 14
			WHEN 'GC1_RESIDUE_C6_PLUS' THEN 10
			WHEN 'GC1_RESIDUE_CO2' THEN 2
			WHEN 'GC1_RESIDUE_IC4' THEN 6
			WHEN 'GC1_RESIDUE_IC5' THEN 8
			WHEN 'GC1_RESIDUE_N2' THEN 1
			WHEN 'GC1_RESIDUE_NC4' THEN 7
			WHEN 'GC1_RESIDUE_NC5' THEN 9
			WHEN 'GC1_RESIDUE_REL_DENS' THEN 12
			WHEN 'GC2_YGRADE_C1' THEN 3
			WHEN 'GC2_YGRADE_C2' THEN 4
			WHEN 'GC2_YGRADE_C2_LIQ_VOL' THEN 38
			WHEN 'GC2_YGRADE_C2C3_RATIO' THEN 9
			WHEN 'GC2_YGRADE_C3' THEN 5
			WHEN 'GC2_YGRADE_C6_PLUS' THEN 10
			WHEN 'GC2_YGRADE_IC4' THEN 6
			WHEN 'GC2_YGRADE_IC5' THEN 8
			WHEN 'GC2_YGRADE_NC4' THEN 7
			WHEN 'GC2_YGRADE_NC5' THEN 9
		END AS rptPriority,
	StartDateTime, DateTime,
	CONVERT(date, DateTime) as ActualDate,
	YEAR(CONVERT(date,DateTime)) as ActualYear,
	DATENAME(quarter, CONVERT(date, DateTime)) as ActualQuarter,
	DATENAME(month, CONVERT(date, DateTime)) as ActualMonth,
	MONTH(CONVERT(date, DateTime)) as ActualMonthNumber,
	DAY(CONVERT(date, DateTime)) as ActualDay,
	Value, vValue
		FROM [CFHISSVR02].[Runtime].[dbo].[History]
		WHERE TagName IN ('GC1_INLET_BTU','GC1_INLET_C1','GC1_INLET_C2','GC1_INLET_C2PLUS_GAL','GC1_INLET_C3','GC1_INLET_C3PLUS_GAL','GC1_INLET_C6_PLUS','GC1_INLET_CO2',
		'GC1_INLET_IC4','GC1_INLET_IC5','GC1_INLET_N2','GC1_INLET_NC4','GC1_INLET_NC5','GC1_INLET_SGU','GC1_RESIDUE_BTU','GC1_RESIDUE_C1','GC1_RESIDUE_C2',
		'GC1_RESIDUE_C2_RECOVER','GC1_RESIDUE_C3','GC1_RESIDUE_C3_RECOVER','GC1_RESIDUE_C6_PLUS','GC1_RESIDUE_CO2','GC1_RESIDUE_IC4','GC1_RESIDUE_IC5','GC1_RESIDUE_N2',
		'GC1_RESIDUE_NC4','GC1_RESIDUE_NC5','GC1_RESIDUE_REL_DENS','GC2_YGRADE_C1','GC2_YGRADE_C2','GC2_YGRADE_C2_LIQ_VOL','GC2_YGRADE_C2C3_RATIO','GC2_YGRADE_C3',
		'GC2_YGRADE_C6_PLUS','GC2_YGRADE_IC4','GC2_YGRADE_IC5','GC2_YGRADE_NC4','GC2_YGRADE_NC5')
		AND wwRetrievalMode = 'Cyclic'
		AND wwResolution = 86400000
		AND wwQualityRule = 'Extended'
		AND wwVersion = 'Latest'
		AND DateTime >= @StartDate
		AND DateTime <= @EndDate) temp 
	WHERE temp.StartDateTime >= @StartDate
	AND temp.Value IS NOT NULL
	AND temp.ActualDate <> '09/13/2020';