
Source Audit Columns -> Nature of the source data. 
Nature of source data
1. Full snapshot of source data
2. CDC data of source for certain period. (day, week etc)
3. Complete transactions as of date
4. Transactions for period (day, week etc)
Only required columns from below list to be included in staging table which holds raw data.
	SrcSnpshtTmstmp
	SrcExtrctFrmTmstmp
	SrcExtrctToTmstmp
	CreatedBySrc
	UpdBySrc
DW Audit Columns -> When record is created/Updated in DW. -> Should Not used by any query/ data processing
	DWCreateTmstmp
	DWUpdTmstmp
DW History columns ->
	DWRowEffDte
	DWRowExpDte
	DWActvRowInd - Active/Expired <CURRENT/ACTIVE>
DW Temporary Table Columns ->
	DWCDCInd ->
		New Row/Record-> I in All SCD implmentations
		Update to existing record -> U [ Table may be SCD1,2,7]
					U(D+I) -> In SCD1 attribute implementations
					U(D+I) + I -> In SCD2 attribute implementations
		Deleted record at source side -> U/Ignore Processing based on approach
				Check with the business/source if soft delete approach needs to be used
				Or it should be ignored to keep record active.
DW Purging and Archiving Columns -> Should Not used by any query/ data processing [Hive archive purge partitions]
	Month -> DWRowExpMnth
	Year  -> DWRowExpYear
DW Partitions for <History Maintainance> -> 
	DWRowExpDte -> 3499-12-31 -> Indicates open records
	DWRowEffDte - For PIT - How to include it in partition ?
	----DWRowExpMnth -> If Integer combine <year and month> - It should be mathematical - 201813->2018
	----DWRowExpYear

	
PseudoCode
1. Create a partitioned table on history columns
2. Compare new source records with target records
3. Update (Here Purge/Insert) New and open records ( Open Records )
3. Insert old records into another partition     ( Closed Records )
4. Check for soft delete is required in case record is not present in the latest snapshot of source.


SCD problems:
1	As Is data
2	Maintain history
3	Maintain current and historical record in same row
4	Frequent update - create <min dim>
5	Access <min dim data> from dim itself. Store Current min dim record key to facilitate this
6	type 1 and typ2 in same table. Use 1,2,3 SCDs. <Current> and historical record for each type2 attr.
7	Multiple typ2 attr. Use <view> to show current data of dim. Store it in FCT as well for easy access to Current value of attribute.

7 for bigdata?

type 7 for bigdata
FCT
SCD2Key - Unique across table - Join directly [Delivers as-on reporting]
SCD1Key Durable key- Unique across open records - Join with open records of dim
NK
DIM
SCD2Key - Unique across table - Join directly
SCD1Key Durable key- Unique across open records - Join with open records of dim
NK


<Work in progress Block Start>
Open records?

e.g. check if cutomer is residing at "XY" location, check if customer has purchased goods worth more than "15$" when he was residing at "LX" location.

Use SCD2key and SCD1key

SCD1key to check for "XY" location - Current As-On Snapshot
SCD2key to check for "LX" location, purchased goods worth more than "15$" ->PIT snapshot

<Work in progress Block End>
